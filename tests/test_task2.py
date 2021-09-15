from unittest.mock import patch
import pytest
import requests
from homework4.task2 import count_dots_on_i


def test_count_dots_on_i():
    with patch('requests.get') as rg:
        rg.return_value.text = 'beautiful life'
        assert count_dots_on_i('link') == 2


def test2_count_dots_on_i():
    with patch('requests.get') as rg:
        rg.return_value.text = 'iiii'
        assert count_dots_on_i("link2") == 4


def test3_count_dots_on_i():
    with patch('requests.get') as rg:
        rg.return_value.text = 'abcdefg'
        assert count_dots_on_i("link3") == 0


def test4_count_dots_on_i():
    with patch('requests.get') as rg:
        rg.return_value.text = 'presentation'
        assert count_dots_on_i("link4") != 6


def test5_count_dots_on_i():
    with patch('requests.get', side_effect=requests.exceptions.RequestException) as rg:
        rg.return_value.text = 'abcdefg'
        with pytest.raises(ValueError):
            count_dots_on_i("https://example.com")

