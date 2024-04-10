class Point:
    def __new__(cls, *args, **kwargs):
        print(f'Создание экземпляра {cls.__name__}')
        instance = super().__new__(cls)
        return instance

    def __init__(self):
        print(f'Вызов __init__ {self.__class__.__name__}')


class Person:
    def __new__(cls, *args, **kwargs):
        print(f'Создание экземпляра {cls.__name__}')
        instance = Point()
        return instance

    def __init__(self):
        print(f'Инициализация экземпляра {self.__class__.__name__}')


p = Person()