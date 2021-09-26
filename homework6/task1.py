"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""


def instances_counter(cls):
    cls.__counter = 0

    def __new__(cls, *args, **kwargs):
        obj = super(cls, cls).__new__(cls)
        cls.__counter += 1
        return obj

    def get_created_instances():
        return cls.__counter

    def reset_instances_counter():
        count_before_reset = cls.__counter
        cls.__counter = 0
        return count_before_reset

    setattr(cls, "__new__", __new__)
    setattr(cls, "get_created_instances", get_created_instances)
    setattr(cls, "reset_instances_counter", reset_instances_counter)

    return cls
