import os
from homework4.task1 import read_magic_number
import pytest


@pytest.fixture()
def temporary_file(tmp_path):
    def file(body):
        file_path = os.path.join(tmp_path, 'test')
        with open(file_path, 'w') as f:
            f.write(body)
        return file_path
    return file


def test_read_magic_number(temporary_file):
    assert read_magic_number(temporary_file('2'))


def test2_read_magic_number(temporary_file):
    assert not read_magic_number(temporary_file('5'))


def test3_read_magic_number(temporary_file):
    assert read_magic_number(temporary_file('3'))


def test4_read_magic_number(temporary_file):
    with pytest.raises(ValueError):
        read_magic_number(temporary_file('a'))


def test5_read_magic_number():
    with pytest.raises(FileExistsError):
        read_magic_number('abcdefg')