from typing import Any, Generator, Hashable, Optional

from algorithms.task2.map import Map


class HashMap(Map):

    def _get_position(self, key: Hashable, key_hash: Optional[int] = None) -> Optional[int]:
        if key_hash is None:
            key_hash = self.hash(key)

        if self._key_val_table[key_hash] is None:
            return None

        for i, (i_key, i_value) in enumerate(self._key_val_table[key_hash]):
            if i_key == key and type(i_key) == type(key):
                return i

        return None

    def __setitem__(self, hashable_key: Hashable, value: Any) -> None:
        key_hash = self.hash(hashable_key)
        exist_key = self._get_position(hashable_key, key_hash)

        if exist_key is None:
            self._len += 1
            try:
                self._key_val_table[key_hash].append((hashable_key, value))
            except AttributeError:
                self._key_val_table[key_hash] = [(hashable_key, value)]
        else:
            self._key_val_table[key_hash][exist_key] = (hashable_key, value)

        self._fix_map_size()

    def __getitem__(self, hashable_key: Hashable) -> Optional[Any]:
        key_hash = self.hash(hashable_key)
        exist_key = self._get_position(hashable_key, key_hash)

        if exist_key is None:
            raise KeyError(hashable_key)
        else:
            return self._key_val_table[key_hash][exist_key][1]

    def __iter__(self):
        return self.keys()

    def __delitem__(self, hashable_key: Hashable):
        key_hash = self.hash(hashable_key)
        i = self._get_position(hashable_key, key_hash)

        if i is None:
            raise KeyError(hashable_key)

        self._key_val_table[key_hash].pop(i)
        self._len -= 1

        if len(self._key_val_table[key_hash]) == 0:
            self._key_val_table[key_hash] = None

        self._fix_map_size()

    def _fix_map_size(self):
        percent = self._len / self._size

        if percent > self._threshold:
            size = self._size * 2
        elif percent < self._threshold / 2 and self._size >= 16:
            size = self._size // 2
        else:
            return

        new_key_val_table = [None] * size

        for key, value in self.items():
            key_hash = hash(key) % size

            try:
                new_key_val_table[key_hash].append((key, value))
            except AttributeError:
                new_key_val_table[key_hash] = [(key, value)]

        self._size = size
        self._key_val_table = new_key_val_table
            
    def values(self) -> Generator[Any, None, None]:
        return (el[1] for sub_list in self._key_val_table if sub_list is not None for el in sub_list)

    def keys(self) -> Generator[Hashable, None, None]:
        return (el[0] for sub_list in self._key_val_table if sub_list is not None for el in sub_list)

    def items(self) -> Generator[tuple[Hashable, Any], None, None]:
        return (el for sub_list in self._key_val_table if sub_list is not None for el in sub_list)
