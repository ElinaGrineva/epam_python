import sys

from homework3.task1 import cache

path = 'data.txt'


def test_cache():
    @cache(times=2)
    def f():
        return input("? ")

    sys.stdin = open(path, "r")
    for i in range(1, 3):
        f()
        for j in range(2):
            f()
    sys.stdin.close()


def test2_cache():
    @cache(times=4)
    def f():
        return input("? ")

    sys.stdin = open(path, "r")
    for i in range(1, 3):
        f()
        for j in range(4):
            f()
    sys.stdin.close()


def test3_cache():
    @cache(times=1)
    def f():
        return input("? ")

    sys.stdin = open(path, "r")
    for i in range(1, 3):
        f()
        for j in range(1):
            assert f() == str(i)
    sys.stdin.close()

