from homework7.task1 import find_occurrences, example_tree


def test_find_red():
    assert find_occurrences(example_tree, 'RED') == 6


def test_find_value1():
    assert find_occurrences(example_tree, 'value1') == 1


def test_find_blue():
    assert find_occurrences(example_tree, 'BLUE') == 2


def test_find_of():
    assert find_occurrences(example_tree, 'of') == 2


def test_find_key3():
    assert find_occurrences(example_tree, 'key3') == 1