import pytest

from algorithms.task1.search import kmp_search, naive_search, sundays_search


@pytest.mark.parametrize("algorithms", [naive_search, sundays_search, kmp_search])
@pytest.mark.parametrize(
    ["text", "pattern", "exist"],
    [
        ("ABABBCAACCAWACACAWCCA", "BCAACCA", 1),
        ("ACBCDABABBDB", "ABA", 1),
        ("ABABABAB", "AB", 4),
        ("ABABABAB", "ABC", 0),
        ("kfjalkfj", "fja", 1),
    ],
)
def test_search(algorithms, text, pattern, exist):
    actual, counter = algorithms(text=text, pattern=pattern)

    assert exist == actual
