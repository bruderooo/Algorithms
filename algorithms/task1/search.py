from itertools import starmap, zip_longest
from operator import eq

from algorithms.task1.utils import create_position_dict, build_help_table


def python_naive_search(text: str, pattern: str) -> int:
    return sum(
        1
        for i in range(len(text) - len(pattern) + 1)
        if all(starmap(eq, zip(text[i:], pattern)))
    )


def naive_search(text: str, pattern: str) -> int:
    no_patterns = 0
    pattern_len = len(pattern)
    text_len = len(text)

    for i in range(text_len - pattern_len + 1):
        check = True
        for text_el, pattern_el in zip_longest(text[i:i + pattern_len], pattern):
            if text_el != pattern_el or text_el is None:
                check = False
                break

        if check:
            no_patterns += 1

    return no_patterns


def sundays_search(text: str, pattern: str) -> int:
    no_patterns = 0
    position_dict = create_position_dict(pattern)
    pattern_len = len(pattern)
    text_len = len(text)
    i = 0

    while True:
        check = True
        for text_el, pattern_el in zip_longest(text[i:i+pattern_len], pattern):
            if text_el != pattern_el or text_el is None:
                check = False
                break

        if check:
            no_patterns += 1

        if i + pattern_len >= text_len:
            return no_patterns

        i += position_dict.get(text[i + pattern_len], pattern_len) + 1


def kmp_search(text: str, pattern: str) -> int:
    text_len = len(text)
    pattern_len = len(pattern)
    help_table = build_help_table(pattern, pattern_len)

    no_patterns = 0
    j = 0
    k = 0

    while j < text_len:
        if pattern[k] == text[j]:
            j += 1
            k += 1
            if k == pattern_len:
                no_patterns += 1
                k = help_table[k]
        else:
            k = help_table[k]
            if k < 0:
                j += 1
                k += 1

    return no_patterns
