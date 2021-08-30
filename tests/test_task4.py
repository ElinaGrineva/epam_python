from homework1.task4 import check_sum_of_four


def test_check_sum_of_four():
    assert check_sum_of_four([0, 2, 4], [6, 8, 10], [-6, -10, -12], [-0, -16, -18]) == 16
