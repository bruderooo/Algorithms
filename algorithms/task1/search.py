from itertools import starmap, zip_longest
from operator import eq


def python_naive_search(text: str, pattern: str) -> int:
    return sum(
        1
        for i in range(len(text) - len(pattern) + 1)
        if all(starmap(eq, zip(text[i:], pattern)))
    )


def naive_search(text: str, pattern: str) -> int:
    no_patterns = 0
    pattern_len = len(pattern)

    for i in range(len(text) - pattern_len + 1):
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
    i = 0

    while True:
        check = True
        for text_el, pattern_el in zip_longest(text[i:i+pattern_len], pattern):
            if text_el != pattern_el or text_el is None:
                check = False
                break

        if check:
            no_patterns += 1

        if i + pattern_len >= len(text):
            return no_patterns

        i += position_dict.get(text[i + pattern_len], pattern_len) + 1


def create_position_dict(pattern: str) -> dict[str, int]:
    reversed_pattern = pattern[::-1]
    unique_pattern = set(pattern)

    return {
        letter: reversed_pattern.find(letter)
        for letter in unique_pattern
    }
