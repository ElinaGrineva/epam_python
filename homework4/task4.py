"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command
You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]
* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""

from typing import List


def fizzbuzz(n: int) -> List[str]:
    res = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            res.append("fizzbuzz")
        elif i % 3 == 0:
            res.append("fizz")
        elif i % 5 == 0:
            res.append("buzz")
        else:
            res.append(str(i))
    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()