import contextlib
from collections.abc import Generator

import pytest

from algorithms.task2.hashmap import HashMap


@pytest.fixture
def hash_map():
    key = [1, 1.5, "a", True]
    value = ["b", 2.7, 4, False]
    hash_map = HashMap(4)

    for key, value in zip(key, value):
        hash_map[key] = value

    return hash_map


@pytest.mark.parametrize("key", [1, 1.5, "a", True])
@pytest.mark.parametrize("value", ["b", 2.7, 4, False])
def test_set_item(key, value):
    size = 8
    hash_map = HashMap(size)
    hash_map[key] = value
    correct_position = hash(key) % size

    assert (key, value) == hash_map._key_val_table[correct_position][0]


@pytest.mark.parametrize("size", [2, 4, 8])
def test_get_item(size, hash_map):
    assert "b" == hash_map[1]
    assert 2.7 == hash_map[1.5]
    assert 4 == hash_map["a"]
    assert False is hash_map[True]


def test_same_key():
    hash_map = HashMap(8)
    hash_map[10] = 4
    hash_map[10] = "a"

    assert "a" == hash_map[10][0]
    assert 1 == len(hash_map[10])


def test_items(hash_map):
    expected = set(zip([1, 1.5, "a", True], ["b", 2.7, 4, False]))

    actual = hash_map.items()

    assert isinstance(actual, Generator)
    assert expected == set(actual)


def test_keys(hash_map):
    expected = {1, 1.5, "a", True}

    actual = hash_map.keys()

    assert isinstance(actual, Generator)
    assert expected == set(actual)


def test_values(hash_map):
    expected = {"b", 2.7, 4, False}

    actual = hash_map.values()

    assert isinstance(actual, Generator)
    assert expected == set(actual)


def test_key_error(hash_map):
    with pytest.raises(KeyError):
        _ = hash_map["blank"]


@pytest.mark.parametrize(
    ["key", "get_context"],
    [
        (1, contextlib.nullcontext()),
        (-1, pytest.raises(KeyError)),
    ]
)
def test_delete(key, get_context, hash_map):
    with get_context:
        del hash_map[key]

    with pytest.raises(KeyError):
        _ = hash_map[key]


def test_resize(hash_map):
    for i in range(2, 10):
        hash_map[i] = i ** 2

    assert 12 == len(hash_map)
    assert 32 == hash_map._size
