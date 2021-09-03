from homework1.task5 import find_maximal_subarray_sum


def test_find_maximal_subarray_sum():
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16


def test2_find_maximal_subarray_sum():
    assert find_maximal_subarray_sum([0, 0, 0, 0, 0, 0], 0) == 0


def test3_find_maximal_subarray_sum():
    assert find_maximal_subarray_sum([-3, -5, -7, -1, -4, -10], -5) == 0


def test4_find_maximal_subarray_sum():
    assert find_maximal_subarray_sum([-4, 1, 3, 4, 6, 1, 5], 7) == 16


def test5_find_maximal_subarray_sum():
    assert find_maximal_subarray_sum([-4, 1, 3, 4, 6, 1, 5], 0) == 0
