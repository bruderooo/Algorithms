from typing import Any, Hashable

HashTableType = list[list[tuple[Hashable, Any]] | None]


def hash_sized(key: Any, size: int):
    return hash(key) % size


def next_pow_2(integer):
    binary = format(integer, "b")
    return int(f"1{'0' * (len(binary) if binary.count('1') > 1 else binary.index('1'))}", 2)


def count(table: HashTableType) -> int:
    return sum(len(el) for el in table if el is not None)


def _insert_item(key: Hashable, value: Any, size: int, key_val_table: HashTableType):
    key_hash = hash_sized(key, size)

    try:
        key_val_table[key_hash].append((key, value))
    except AttributeError:
        key_val_table[key_hash] = [(key, value)]
