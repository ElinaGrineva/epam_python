from homework1.task3 import find_maximum_and_minimum

path = 'files_for_test/'


def test_find_maximum_and_minimum():
    assert find_maximum_and_minimum(path + 'some_file.txt') == (0, 0)


def test2_find_maximum_and_minimum():
    assert find_maximum_and_minimum(path + 'some_file2.txt') == (5, 5)


def test3_find_maximum_and_minimum():
    assert find_maximum_and_minimum(path + 'some_file3.txt') == (-74849498474, 3998)

