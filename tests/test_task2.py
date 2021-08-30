from homework1.task2 import check_fibonacci


def test_check_fibonacci():
    assert check_fibonacci([0, 1, 2, 3, 5, 8, 5, 21, 34, 57]) is False


def test2_check_fibonacci():
    assert check_fibonacci([1, 2]) is True

