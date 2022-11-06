from typing import Hashable


def hash_sized(key: Hashable, size: int, i: int = 0):
    return (hash(key) + i) % size


def next_pow_2(integer):
    binary = format(integer, "b")
    return int(f"1{'0' * (len(binary) if binary.count('1') > 1 else binary.index('1'))}", 2)
