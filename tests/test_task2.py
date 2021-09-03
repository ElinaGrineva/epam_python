from homework2.task2 import major_and_minor_elem


def test1_major_and_minor_elem():
    assert major_and_minor_elem([3, 2, 3]) == (3, 2)


def test2_major_and_minor_elem():
    assert major_and_minor_elem([2, 2, 1, 1, 1, 2, 2]) == (2, 1)


def test3_major_and_minor_elem():
    assert major_and_minor_elem([[-5, -5, -5, -5, -1, 0, 0]]) == (-5, -1)



