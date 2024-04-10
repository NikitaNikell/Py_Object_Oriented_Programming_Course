class Person(object, metaclass=type):

    """ Аргумент metaclass позволяет нам указать, какой класс мы хотим использовать для создания нашего класса.
    Таким образом, мы могли бы создать собственный класс, который будет создавать новый тип данных, внедряя в процесс
    создания любую функциональность, которую мы хотим. Это позволит нам изменять определение/функциональность класса,
    который мы создаем, с помощью кода."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        return f'Hi, I am {self.name}. I am {self.age} year old.'


class Student(Person, metaclass=type):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major


#Какова основная цель метаклассов в python? = Настроить создание классов