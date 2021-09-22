import pytest
from homework6.task2 import DeadlineError, HomeworkResult, Student, Teacher


def test_deadline_error():
    opp_teacher = Teacher("Daniil", "Shadrin")
    lazy_student = Student("Roman", "Petrov")
    oop_hw = opp_teacher.create_homework("Learn OOP", 0)
    with pytest.raises(DeadlineError, match="You are late"):
        lazy_student.do_homework(oop_hw, "Lazy student have done this work")


def test_homework_result_type_error():
    good_student = Student("Lev", "Sokolov")
    with pytest.raises(TypeError, match="You gave a not Homework object"):
        HomeworkResult(good_student, "fff", "Solution")


def test_lazy_student_not_in_homework_done():
    opp_teacher = Teacher("Daniil", "Shadrin")
    lazy_student = Student("Roman", "Petrov")
    docs_hw = opp_teacher.create_homework("Read docs", 5)
    result_3 = lazy_student.do_homework(docs_hw, "done")
    opp_teacher.check_homework(result_3)
    assert (lazy_student, "done") not in Teacher.homework_done[docs_hw]


def test_good_student_in_homework_done():
    opp_teacher = Teacher("Daniil", "Shadrin")
    good_student = Student("Lev", "Sokolov")

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    docs_hw = opp_teacher.create_homework("Read docs", 5)

    result_1 = good_student.do_homework(oop_hw, "I have done this hw")
    result_2 = good_student.do_homework(docs_hw, "I have done this hw too")

    opp_teacher.check_homework(result_1)
    opp_teacher.check_homework(result_2)

    assert (good_student, "I have done this hw") in \
        Teacher.homework_done[oop_hw]
    assert (good_student, "I have done this hw too") in \
        Teacher.homework_done[docs_hw]


def test_homework_done():
    opp_teacher = Teacher("Daniil", "Shadrin")
    teacher = Teacher("Aleksandr", "Smetanin")

    good_student = Student("Lev", "Sokolov")

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)

    result_1 = good_student.do_homework(oop_hw, "I have done this hw")

    opp_teacher.check_homework(result_1)
    temp1 = opp_teacher.homework_done
    teacher.check_homework(result_1)
    temp2 = Teacher.homework_done

    assert temp1 == temp2
    assert len(Teacher.homework_done[oop_hw]) == 1