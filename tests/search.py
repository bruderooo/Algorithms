from algorithms.task1.search import create_position_dict, naive_search, sundays_search, python_naive_search

import pytest

def test_create_position_dict():
    expected = {"A": 1, "B": 7, "C": 2}
    pattern = "BCAACCA"

    actual = create_position_dict(pattern)

    assert expected == actual


@pytest.mark.parametrize(
    "algorithms",
    [python_naive_search, naive_search, sundays_search]
)
@pytest.mark.parametrize(
    ["text", "pattern", "exist"],
    [
        ("ABABBCAACCAWACACAWCCA", "BCAACCA", 1),
        ("ACBCDABABBDB", "ABA", 1),
        ("ABABABAB", "AB", 4),
        ("ABABABAB", "ABC", 0),
        ("kfjalkfj", "fja", 1),
    ]
)
def test_search(algorithms, text, pattern, exist):

    actual = algorithms(text=text, pattern=pattern)

    assert exist == actual
