import pytest
from homework9.task3 import universal_file_counter


@pytest.fixture()
def create_files(tmpdir):

    def create_file(*body):
        for element in body:
            file = tmpdir.join('my_file'+str(len(tmpdir.listdir()))+'.txt')
            file.write(element)
        return tmpdir.strpath

    return create_file


@pytest.fixture()
def test_create_file_1(create_files):
    return create_files('1\n3 5\n5 6 7', '2\n4\n6\n8')


def test_no_tokenizer(test_create_file_1):
    assert universal_file_counter(test_create_file_1, 'txt') == 7


def test_with_tokenizers(test_create_file_1):
    assert universal_file_counter(test_create_file_1, 'txt', str.split) == 10
