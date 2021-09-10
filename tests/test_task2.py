from homework1.task2 import check_fibonacci


def test_check_fibonacci():
    assert check_fibonacci([2, 3, 5, 1, 34, 5, 6]) is False


def test2_check_fibonacci():
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]) is True

