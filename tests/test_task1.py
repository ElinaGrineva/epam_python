from homework6.task1 import instances_counter


@instances_counter
class User:
    pass


def test_get_created_instances():
    count = User.get_created_instances()
    assert count == 0


def test2_get_created_instances():
    user, _, _ = User(), User(), User()
    count = User.get_created_instances()
    assert count == 3


def test_reset_instances_counter():
    user, _, _ = User(), User(), User()
    count_before = user.reset_instances_counter()
    assert count_before == 3