import contextlib

import pytest

from algorithms.task2.chainhashmap import ChainHashMap
from algorithms.task2.openhashmap import OpenHashMap


@pytest.fixture
def open_hash_map():
    key = [1, 1.5, "a", True]
    value = ["b", 2.7, 4, False]
    hash_map = OpenHashMap(size=8)

    for key, value in zip(key, value):
        hash_map[key] = value

    return hash_map


@pytest.fixture
def chain_hash_map():
    key = [1, 1.5, "a", True]
    value = ["b", 2.7, 4, False]
    hash_map = ChainHashMap(size=8)

    for key, value in zip(key, value):
        hash_map[key] = value

    return hash_map


@pytest.fixture(params=[
    'open_hash_map',
    'chain_hash_map'
])
def map_obj(request):
    return request.getfixturevalue(request.param)


@pytest.mark.parametrize("key", [1, 1.5, "a", True])
@pytest.mark.parametrize("value", ["b", 2.7, 4, False])
def test_set_item(key, value):
    size = 8
    hash_map = ChainHashMap(size)
    hash_map[key] = value
    correct_position = hash(key) % size

    assert (key, value) == hash_map._key_val_table[correct_position][0]


def test_get_item(map_obj):
    assert "b" == map_obj[1]
    assert 2.7 == map_obj[1.5]
    assert 4 == map_obj["a"]
    assert False is map_obj[True]


@pytest.mark.parametrize('map_type', [ChainHashMap, OpenHashMap])
def test_same_key(map_type):
    hash_map = map_type(8)
    hash_map[10] = 4
    hash_map[10] = "a"

    assert "a" == hash_map[10]


def test_items(map_obj):
    expected = set(zip([1, 1.5, "a", True], ["b", 2.7, 4, False]))

    actual = map_obj.items()

    assert expected == set(actual)


def test_keys(map_obj):
    expected = {1, 1.5, "a", True}

    actual = map_obj.keys()

    assert expected == set(actual)


def test_values(map_obj):
    expected = {"b", 2.7, 4, False}

    actual = map_obj.values()

    assert expected == set(actual)


def test_key_error(map_obj):
    with pytest.raises(KeyError):
        _ = map_obj["blank"]


@pytest.mark.parametrize(
    ["key", "get_context"],
    [
        (1, contextlib.nullcontext()),
        (-1, pytest.raises(KeyError)),
    ],
)
def test_delete(key, get_context, map_obj):
    with get_context:
        del map_obj[key]

    with pytest.raises(KeyError):
        _ = map_obj[key]


def test_resize(map_obj):
    for i in range(2, 10):
        map_obj[i] = i ** 2

    assert 12 == len(map_obj)
    assert 32 == map_obj._size


def test_resize_to_smaller(map_obj):
    del map_obj[1]

    assert 3 == len(map_obj)
    assert 8 == map_obj._size


def test(map_obj):
    hashmap = OpenHashMap(8)
    hashmap[1] = "a"
    hashmap[9] = "b"

    del hashmap[1]

    assert hashmap[9] == "b"
