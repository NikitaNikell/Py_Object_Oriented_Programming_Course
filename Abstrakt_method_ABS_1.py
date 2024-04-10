from abc import ABC, abstractmethod

""" Абстрактный метод - это метод, который объявлен в абстрактном классе, но не имеет реализации. 
Он служит как бы шаблоном для метода, который должен быть реализован в подклассах. """

class Animal(ABC):

    """ В Python абстрактные классы реализуются с помощью модуля abc (аббревиатура от Abstract Base Classes).
    Для создания абстрактного класса нам понадобиться класс ABC, а для создания абстрактного метода - декоратор
    abstractmethod. Оба эти объекта импортируются из стандартного модуля abc"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


class Bird(Animal):
    def make_sound(self):
        return "Tweet!"


def animal_sounds(animals):
    for animal in animals:
        print(animal.name + " says " + animal.make_sound())


dog = Dog("Sharik", 2)
cat = Cat("Barsik", 4)
bird = Bird("Kesha", 1)

animal_sounds([dog, cat, bird])

#!!!!! Если не реализовать абстрактный метод в дочернем классе, возникнет ошибка при вызове класса.