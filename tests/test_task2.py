from homework9.task2 import Supressor, supressor_gen
import pytest


def test_supressor_class_passed_exception():
    with Supressor(IndexError):
        [][2]


def test_supressor_gen_passed_exception():
    with supressor_gen(IndexError):
        [][2]


def test_supressor_class_positive():
    with Supressor(ValueError):
        raise ValueError


def test_supressor_class_raise_error():
    with Supressor(ValueError):
        with pytest.raises(AttributeError):
            raise AttributeError


def test_supressor_gen_positive():
    with supressor_gen(ValueError):
        raise ValueError


def test_supressor_gen_raise_error():
    with supressor_gen(ValueError):
        with pytest.raises(AttributeError):
            raise AttributeError