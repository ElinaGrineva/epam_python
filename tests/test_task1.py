import pytest
from homework9.task1 import merge_sorted_files


@pytest.fixture()
def create_files(tmpdir):

    def create_file(*body):
        for element in body:
            file = tmpdir.join('my_file'+str(len(tmpdir.listdir())))
            file.write(element)
        return tmpdir.listdir()

    return create_file


@pytest.fixture()
def create_data_1(create_files):
    return create_files('1\n3\n5', '2\n4\n6')


@pytest.fixture()
def create_data_2(create_files):
    return create_files('1\n1\n6\n8\n10', '2\n3\n5\n7\n11')


def test_1(create_data_1):
    assert list(merge_sorted_files(create_data_1)) == \
           [1, 2, 3, 4, 5, 6]


def test_2(create_data_2):
    assert list(merge_sorted_files(create_data_2)) == \
           [1, 1, 2, 3, 5, 6, 7, 8, 10, 11]