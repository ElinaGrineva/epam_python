import string
from homework2.task5 import custom_range


def test1_custom_range():
    assert custom_range(string.ascii_lowercase, "g") == ['a', 'b', 'c', 'd', 'e', 'f']


def test2_custom_range():
    assert custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']


def test3_custom_range():
    assert custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
