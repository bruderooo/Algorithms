import csv
import string
from random import choices
from time import perf_counter_ns

import pandas as pd
import seaborn as sns


def create_position_dict(pattern: str) -> dict[str, int]:
    reversed_pattern = pattern[::-1]
    unique_pattern = set(pattern)

    return {letter: reversed_pattern.find(letter) for letter in unique_pattern}


def build_help_table(word: str, word_len: int) -> list[int]:
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


def load_and_plot(name: str):
    df = pd.read_csv(f"{name}.csv")
    return sns.pointplot(data=df, x=name, y="time[ns]", hue="function", errorbar=None, scale=0.6)


def generate(dictionary: str = string.ascii_letters, length: int = 50) -> str:
    return "".join(choices(dictionary, k=length))


def create_csv(value_name: str):
    with open(f"{value_name}.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(("count", value_name, "function", "time[ns]"))


def compute(
    functions: list,
    text: str,
    pattern: str,
    value_name: str,
    value: int,
):
    for func in functions:
        start_time = perf_counter_ns()
        count = func(text=text, pattern=pattern)
        end_time = perf_counter_ns()

        with open(f"{value_name}.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow((count, value, func.__name__, end_time - start_time))
