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


if __name__ == "__main__":
    print(lcs("ababc", "abc"))
