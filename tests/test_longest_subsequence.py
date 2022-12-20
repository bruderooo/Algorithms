import pytest

from algorithms.task3.longest_subsequence import lcs, lcs_lower_memory, lcs_with_cached_table


@pytest.fixture
def sequence_first():
    return list(range(0, 10))


@pytest.fixture
def sequence_second():
    return list(range(4, 20))


def test_longest_subsequence(sequence_first, sequence_second):
    expected = [4, 5, 6, 7, 8, 9]

    actual = lcs(sequence_first, sequence_second)

    assert expected == actual


def test_longest_subsequence_cached(sequence_first, sequence_second):
    expected = [4, 5, 6, 7, 8, 9]

    actual = lcs_with_cached_table(sequence_first, sequence_second)

    assert expected == actual


def test_lcs_lower_memory(sequence_first, sequence_second):
    expected = [4, 5, 6, 7, 8, 9]

    actual = lcs_lower_memory(sequence_first, sequence_second)

    assert expected == actual
