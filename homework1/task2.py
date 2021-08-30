"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""

from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    if len(data) < 3:
        return True
    for el in data:
        if data.index(el) > 1:
            if el != data[data.index(el)-1]+data[data.index(el)-2]:
                return False
    return True