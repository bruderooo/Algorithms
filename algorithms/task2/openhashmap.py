from typing import Any

from algorithms.task2.map import Map
from algorithms.task2.utils import hash_sized, next_pow_2


class OpenHashMap(Map):
    def __eq__(self, other):
        pass

    def __setitem__(self, key, value) -> None:
        self.insert(key, value)

    def insert(self, key, value):
        for i in range(self._size):
            key_hash = hash_sized(key, self._size, i)

            if (
                (element := self._key_val_table[key_hash]) is None
                or (element[0] == key and type(element[0]) == type(key))
            ):
                self._key_val_table[key_hash] = (key, value)
                self._fix_map_size()
                break

    def __getitem__(self, key) -> Any:
        for i in range(self._size):
            key_hash = hash_sized(key, self._size, i)

            if (
                (element := self._key_val_table[key_hash]) is not None
                and element[0] == key
                and type(element[0]) == type(key)
            ):
                self._fix_map_size()
                return element[1]

        raise KeyError(key)

    def __delitem__(self, key):
        for i in range(self._size):
            key_hash = hash_sized(key, self._size, i)

            if (
                (element := self._key_val_table[key_hash]) is not None
                and element[0] == key
                and type(element[0]) == type(key)
            ):
                self._key_val_table[key_hash] = None
                self._fix_map_size()
                return

        raise KeyError(key)

    def _fix_map_size(self):
        percent = len(self) / self._size

        if percent > self._threshold:
            size = self._size * 2
        elif percent < self._threshold / 2 and self._size >= 16:
            size = self._size // 2
        else:
            return

        size = next_pow_2(size)
        new_key_val_table = [None] * size

        for key, value in self.items():
            for i in range(size):
                key_hash = hash_sized(key, size, i)

                if (
                        (element := new_key_val_table[key_hash]) is None
                        or (element[0] == key and type(element[0]) == type(key))
                ):
                    new_key_val_table[key_hash] = (key, value)
                    break

        self._size = size
        self._key_val_table = new_key_val_table

    def items(self):
        return filter(lambda item: item is not None, self._key_val_table)

    def keys(self):
        return (item[0] for item in self._key_val_table if item is not None)

    def values(self):
        return (item[1] for item in self._key_val_table if item is not None)

    def __len__(self):
        return sum(1 for el in self._key_val_table if el is not None)

