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
