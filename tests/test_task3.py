from homework7.task3 import tic_tac_toe_checker


def test_x_win():
    assert tic_tac_toe_checker(([['-', '-', 'o'],
                                 ['-', 'o', 'o'],
                                 ['x', 'x', 'x']])) == 'x wins!'


def test_o_win():
    assert tic_tac_toe_checker([['-', '-', 'o'],
                                ['-', 'x', 'o'],
                                ['x', 'x', 'o']]) == 'o wins!'


def test_draw():
    assert tic_tac_toe_checker([['o', 'x', 'o'],
                                ['o', 'x', 'o'],
                                ['x', 'o', 'x']]) == 'draw!'


def test_unfinished():
    assert tic_tac_toe_checker([['-', '-', 'o'],
                                ['-', 'x', 'o'],
                                ['x', 'o', 'x']]) == 'unfinished'
