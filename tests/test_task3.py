from homework4.task3 import my_precious_logger


def test_my_precious_logger(capsys):
    my_precious_logger('error: file not found\n')
    fixed = capsys.readouterr()
    assert fixed.err == 'error: file not found\n'


def test2_my_precious_logger(capsys):
    my_precious_logger('OK\n')
    fixed = capsys.readouterr()
    assert fixed.out == 'OK\n'


def test3_my_precious_logger(capsys):
    my_precious_logger('error: ValueError Exception')
    fixed = capsys.readouterr()
    assert fixed.out != 'error: ValueError Exception'
