from abc import abstractmethod
from typing import Any, Hashable

from algorithms.task2.utils import HashTableType, count


class Map:
    def __init__(self, size: int = 8, threshold: float = 0.66, key_val_table: HashTableType = None):
        self._size = size

        if key_val_table is None:
            self._key_val_table = [None] * size
        else:
            self._key_val_table = key_val_table

        self._threshold = threshold

    def __len__(self):
        return count(self._key_val_table)

    @abstractmethod
    def __setitem__(self, key, value) -> None:
        raise NotImplementedError()

    @abstractmethod
    def __getitem__(self, item) -> Any:
        raise NotImplementedError()

    def __str__(self):
        return "{" + ", ".join(f"{el[0]}: {el[1]}" for el in self._key_val_table if el is not None) + "}"

    def __eq__(self, other):
        try:
            return all(other[key] == val for key, val in self.items())
        except:
            return False

    @abstractmethod
    def items(self):
        raise NotImplementedError()
