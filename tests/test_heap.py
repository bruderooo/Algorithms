from random import seed, shuffle

import pytest

from algorithms.task4.binary_heap import BinaryHeap


@pytest.fixture
def heap():
    binary_heap = BinaryHeap()
    for el in [(1, "a"), (4, "b"), (7, "c"), (2, "d"), (5, "e")]:
        binary_heap.push(el)
    return binary_heap


@pytest.fixture
def heap_longer():
    seq = list(zip([1, 2, 3, 17, 19, 36, 7, 25, 100], "abcdefghi"))
    seed(1)
    shuffle(seq)
    binary_heap = BinaryHeap()
    for el in seq:
        binary_heap.push(el)
    return binary_heap


def test_heapify(heap):
    assert [(1, "a"), (2, "d"), (7, "c"), (4, "b"), (5, "e")] == heap._heap


def test_heapify_longer(heap_longer):
    assert [
        (1, "a"),
        (2, "b"),
        (7, "g"),
        (3, "c"),
        (19, "e"),
        (25, "h"),
        (100, "i"),
        (36, "f"),
        (17, "d"),
    ] == heap_longer._heap


def test_pop(heap):
    assert (1, "a") == heap.pop()
    assert [(2, "d"), (4, "b"), (7, "c"), (5, "e")] == heap._heap


@pytest.mark.parametrize(
    ("item", "index"),
    (
        [(10, "j"), -1],
        [(1, "k"), 2],
    ),
)
def test_push(heap, item, index):
    heap.push(item)

    assert item == heap._heap[index]
