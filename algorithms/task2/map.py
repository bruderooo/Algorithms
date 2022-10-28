from abc import abstractmethod
from typing import Any, Hashable


class Map:

    def __init__(self, size: int = 8, threshold: float = 0.66):
        self._size = size
        self._key_val_table: list[list[tuple[Hashable, Any]]] = [None] * size
        self._len = 0
        self._threshold = threshold

    def hash(self, key):
        return hash(key) % self._size

    def __len__(self):
        return self._len

    @abstractmethod
    def __setitem__(self, key, value) -> None:
        raise NotImplementedError()

    @abstractmethod
    def __getitem__(self, item) -> Any:
        raise NotImplementedError()

    def __str__(self):
        return "{" + ", ".join(f"{el[0]}: {el[1]}" for el in self._key_val_table if el is not None) + "}"
