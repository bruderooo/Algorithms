from typing import Any, Generator, Hashable

from algorithms.task2.map import Map
from algorithms.task2.utils import hash_sized, next_pow_2


class Deleted:
    pass


def check_element(item: Any) -> bool:
    return item is not None and item is not OpenHashMap.DELETED


class OpenHashMap(Map):
    DELETED: Deleted = Deleted()

    def __setitem__(self, key, value) -> None:
        self.insert(key, value)

    def insert(self, key: Hashable, value: Any):
        for i in range(self._size):
            key_hash = hash_sized(key, self._size, i)

            if (
                (element := self._key_val_table[key_hash]) is None
                or element is OpenHashMap.DELETED
                or (element[0] == key and type(element[0]) == type(key))
            ):
                self._key_val_table[key_hash] = (key, value)
                self._fix_map_size()
                break

    def __getitem__(self, key: Hashable) -> Any:
        for i in range(self._size):
            key_hash = hash_sized(key, self._size, i)

            if (element := self._key_val_table[key_hash]) is not None:
                if element is not OpenHashMap.DELETED and element[0] == key and type(element[0]) == type(key):
                    return element[1]
            else:
                raise KeyError(key)

    def __delitem__(self, key: Hashable):
        for i in range(self._size):
            key_hash = hash_sized(key, self._size, i)

            if (
                (element := self._key_val_table[key_hash]) is not None
                and element is not OpenHashMap.DELETED
                and element[0] == key
                and type(element[0]) == type(key)
            ):
                self._key_val_table[key_hash] = OpenHashMap.DELETED
                self._fix_map_size()
                return

        raise KeyError(key)

    def _fix_map_size(self):
        percent = len(self) / self._size

        if percent > self._threshold:
            size = self._size + 1
        elif percent < self._threshold / 2 and self._size >= 16:
            size = self._size // 2
        else:
            return

        size = next_pow_2(size)
        new_key_val_table = [None] * size

        for key, value in self.items():
            for i in range(size):
                key_hash = hash_sized(key, size, i)

                if (element := new_key_val_table[key_hash]) is None or (
                    element[0] == key and type(element[0]) == type(key)
                ):
                    new_key_val_table[key_hash] = (key, value)
                    break

        self._size = size
        self._key_val_table = new_key_val_table

    def items(self) -> filter:
        return filter(check_element, self._key_val_table)

    def keys(self) -> Generator[Hashable, None, None]:
        return (item[0] for item in self._key_val_table if check_element(item))

    def values(self) -> Generator[Any, None, None]:
        return (item[1] for item in self._key_val_table if check_element(item))

    def __len__(self) -> int:
        return sum(1 for item in self._key_val_table if check_element(item))
