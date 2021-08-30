from homework1.task3 import find_maximum_and_minimum


def test_find_maximum_and_minimum():
    assert find_maximum_and_minimum('../tests/file_for_test/some_file.txt') == (-5, 10)
