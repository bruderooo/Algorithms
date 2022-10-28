import csv
import string
from random import choices
from timeit import default_timer as timer
from typing import Dict, List

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def create_position_dict(pattern: str) -> Dict[str, int]:
    reversed_pattern = pattern[::-1]

    set_to_return = {}

    for i, letter in enumerate(reversed_pattern):
        if letter in set_to_return:
            break
        else:
            set_to_return[letter] = i

    return set_to_return


def build_help_table(word: str, word_len: int) -> List[int]:
    to_return = [-1]
    pos = 1
    cnd = 0

    while pos < word_len:
        if word[pos] == word[cnd]:
            to_return.append(to_return[cnd])
        else:
            to_return.append(cnd)

            while cnd >= 0 and word[pos] != word[cnd]:
                cnd = to_return[cnd]

        pos += 1
        cnd += 1

    to_return.append(cnd)

    return to_return


def load_and_plot(
    name: str, scale: float = 0.6, rotate: int = 0, font_scale: float = 2.
):
    df = pd.read_csv(f"{name}.csv")
    sns.set(font_scale=font_scale)
    fig, ax = plt.subplots(1, 2, figsize=(30, 15))
    sns.pointplot(data=df, x=name, y="time[ns]", hue="function", errorbar=None, scale=scale, ax=ax[0])
    sns.pointplot(data=df, x=name, y="comparisons", hue="function", errorbar=None, scale=scale, ax=ax[1])
    ax[0].tick_params(axis='x', rotation=rotate)
    ax[1].tick_params(axis='x', rotation=rotate)


def generate(dictionary: str = string.ascii_letters, length: int = 50) -> str:
    return "".join(choices(dictionary, k=length))


def create_csv(value_name: str) -> None:
    with open(f"{value_name}.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(("count", value_name, "function", "time[ns]", "comparisons"))


def compute(
    functions: list,
    text: str,
    pattern: str,
    value_name: str,
    value: int,
) -> None:
    for func in functions:
        times = []
        for i in range(20):
            start_time = timer()
            count, comparisons = func(text=text, pattern=pattern)
            end_time = timer()
            times.append(end_time - start_time)

        with open(f"{value_name}.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow((count, value, func.__name__, min(times), comparisons))
