from typing import Any, Generator, Hashable, Optional

from algorithms.task2.map import Map
from algorithms.task2.utils import _insert_item, hash_sized, next_pow_2


class HashMap(Map):
    def _get_position(self, key: Hashable, key_hash: Optional[int] = None) -> Optional[int]:
        if key_hash is None:
            key_hash = hash_sized(key, self._size)

        if self._key_val_table[key_hash] is None:
            return None

        else:
            for i, (i_key, i_value) in enumerate(self._key_val_table[key_hash]):
                if i_key == key and type(i_key) == type(key):
                    return i

            return None

    def __setitem__(self, hashable_key: Hashable, value: Any) -> None:
        key_hash = hash_sized(hashable_key, self._size)

        if (exist_key := self._get_position(hashable_key, key_hash)) is None:
            _insert_item(hashable_key, value, self._size, self._key_val_table)
        else:
            self._key_val_table[key_hash][exist_key] = (hashable_key, value)

        self._fix_map_size()

    def __getitem__(self, hashable_key: Hashable) -> Optional[Any]:
        key_hash = hash_sized(hashable_key, self._size)
        exist_key = self._get_position(hashable_key, key_hash)

        if exist_key is None:
            raise KeyError(hashable_key)
        else:
            return self._key_val_table[key_hash][exist_key][1]

    def __iter__(self):
        return self.keys()

    def __delitem__(self, hashable_key: Hashable):
        key_hash = hash_sized(hashable_key, self._size)
        i = self._get_position(hashable_key, key_hash)

        if i is None:
            raise KeyError(hashable_key)

        self._key_val_table[key_hash].pop(i)

        if len(self._key_val_table[key_hash]) == 0:
            self._key_val_table[key_hash] = None

        self._fix_map_size()

    def _fix_map_size(self):
        percent = len(self) / self._size

        if percent > self._threshold:
            size = self._size * 2
        elif percent < self._threshold / 2 and self._size >= 16:
            size = self._size // 2
        else:
            return

        new_key_val_table = [None] * size

        for key, value in self.items():
            _insert_item(key, value, size, new_key_val_table)

        self._size = size
        self._key_val_table = new_key_val_table

    def values(self) -> Generator[Any, None, None]:
        return (el[1] for sub_list in self._key_val_table if sub_list is not None for el in sub_list)

    def keys(self) -> Generator[Hashable, None, None]:
        return (el[0] for sub_list in self._key_val_table if sub_list is not None for el in sub_list)

    def items(self) -> Generator[tuple[Hashable, Any], None, None]:
        return (el for sub_list in self._key_val_table if sub_list is not None for el in sub_list)

    @classmethod
    def create_from_tuples(cls, keys_values: list[tuple[Any, Any]]):
        size = next_pow_2(len(keys_values))
        new_key_val_table = [None] * size

        for key, value in keys_values:
            _insert_item(key, value, size, new_key_val_table)

        return cls(size=size, key_val_table=new_key_val_table)
