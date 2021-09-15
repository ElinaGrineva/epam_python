from datetime import timedelta
from homework5.task1 import Homework, Student, Teacher

teacher = Teacher("Daniil", "Shadrin")
student = Student("Roman", "Petrov")
create_homework_too = teacher.create_homework
oop_homework = create_homework_too("create 2 simple classes", 5)
expired_homework = teacher.create_homework("Learn functions", 0)


def test_teacher():
    assert teacher.first_name == "Daniil"
    assert teacher.last_name == "Shadrin"


def test_student():
    assert student.first_name == "Roman"
    assert student.last_name == "Petrov"


def test_create_homework():
    assert expired_homework.deadline == timedelta(0)
    assert expired_homework.text == "Learn functions"
    assert isinstance(expired_homework, Homework)


def test_do_homework():
    assert oop_homework.deadline == timedelta(deadline=5)
    assert student.do_homework(oop_homework) is oop_homework
    assert student.do_homework(expired_homework) is None
