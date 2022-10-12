from algorithms.task1.utils import create_position_dict


def test_create_position_dict():
    expected = {"A": 1, "B": 7, "C": 2}
    pattern = "BCAACCA"

    actual = create_position_dict(pattern)

    assert expected == actual


def test_create_csv(tmp_path):
    assert True
