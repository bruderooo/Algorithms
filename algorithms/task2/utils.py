from typing import Hashable


def hash_sized(key: Hashable, size: int, i: int = 0):
    return (hash(key) + i) % size


def next_pow_2(integer):
    binary = format(integer, "b")
    return int(binary if binary.count('1') == 1 else "1" + ("0" * len(binary)), 2)
