from homework7.task2 import backspace_compare


def test_backspace_compare():
    assert backspace_compare("ab#c", "ad#c") is True


def test2_backspace_compare():
    assert backspace_compare("a##c", "#a#c") is True


def test3_backspace_compare():
    assert backspace_compare("a#c", "b") is False
