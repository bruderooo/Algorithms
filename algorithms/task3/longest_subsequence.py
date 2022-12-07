from functools import lru_cache
from typing import Any


def lcs(seq1, seq2):
    @lru_cache(maxsize=None)
    def _lcs(i: int, j: int) -> list[Any]:
        if i == -1 or j == -1:
            return []
        elif seq1[i] == seq2[j]:
            return _lcs(i - 1, j - 1) + [seq1[i]]
        else:
            return max(_lcs(i - 1, j), _lcs(i, j - 1), key=len)

    return _lcs(len(seq1) - 1, len(seq2) - 1)


def lcs_with_cached_table(seq1, seq2):
    cached_table = {}

    def _lcs(i: int, j: int) -> list[Any]:
        if (i, j) not in cached_table:
            if i == -1 or j == -1:
                cached_table[(i, j)] = []
            elif seq1[i] == seq2[j]:
                cached_table[(i, j)] = _lcs(i - 1, j - 1) + [seq1[i]]
            else:
                cached_table[(i, j)] = max(_lcs(i - 1, j), _lcs(i, j - 1), key=len)

        return cached_table[(i, j)]

    _lcs(len(seq1) - 1, len(seq2) - 1)
    return cached_table[(len(seq1) - 1, len(seq2) - 1)]
