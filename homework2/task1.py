"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from collections import Counter
import string
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    with open(file_path, 'r', encoding='unicode-escape') as f:
        text = f.read()
        string_punctuation = string.punctuation
        text = "".join(ch for ch in text if ch not in string_punctuation)
        word_list = text.split()
        word_list = sorted(word_list, key=lambda x: (-len(set(x)), -len(x)))
        return word_list[:10]


def get_rarest_char(file_path: str) -> str:
    with open(file_path, 'r', encoding='unicode-escape') as f:
        text = f.read()
        count = list(Counter(text))
        return count[-1]


def count_punctuation_chars(file_path: str) -> int:
    with open(file_path, 'r', encoding='unicode-escape') as f:
        text = f.read()
        count = sum(1 for el in text if el in string.punctuation)
        return count


def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path, 'r', encoding='unicode-escape') as f:
        text = f.read()
        return sum(1 for el in text if not el.isascii())


def get_most_common_non_ascii_char(file_path: str) -> str:
    with open(file_path, 'r', encoding='unicode-escape') as f:
        text = f.read()
        return Counter(el for el in text if not el.isascii()).most_common()[0][0]

