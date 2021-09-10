from homework2 import task1


def test_get_longest_diverse_words():
    assert task1.get_longest_diverse_words('data.txt') == ['Bevölkerungsabschub', 'Kollektivschuldiger', 'unmißverständliche', 'Werkstättenlandschaft', 'Werkstättenlandschaft', 'Selbstverständlich', 'Schicksalsfiguren', 'Verfassungsverletzungen', 'politischstrategischen', 'Entscheidungsschlacht']


def test_get_rarest_char():
    assert task1.get_rarest_char('data.txt') == '›'


def test_count_punctuation_chars():
    assert task1.count_punctuation_chars('data.txt') == 5305


def test_count_non_ascii_chars():
    assert task1.count_non_ascii_chars('data.txt') == 2972


def test_get_most_common_non_ascii_char():
    assert task1.get_most_common_non_ascii_char('data.txt') == 'ä'
