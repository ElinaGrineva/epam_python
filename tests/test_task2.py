from functools import reduce
from homework5.task2 import print_result


@print_result
def custom_sum(*args):
    return reduce(lambda x, y: x + y, args)


def test__doc__():
    assert custom_sum.__doc__ == "None"


def test__name__():
    assert custom_sum.__name__ == "custom_sum"


def test_has_atr__original_func():
    assert hasattr(custom_sum, "__original_func") is True


def test__original_func():
    with_print = print_result(sum)
    assert with_print.__original_func == sum


