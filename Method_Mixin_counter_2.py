class CountInstancesMixin:
    count = 0

    def __new__(cls, *args, **kwargs):
        cls.count += 1


class Cat(CountInstancesMixin):
    def __init__(self, name):
        self.name = name


class Dog(CountInstancesMixin):
    def __init__(self, name):
        self.name = name


# Котики
obj1 = Cat("Барсик")
obj2 = Cat("Гипард")
# Собаки
obj3 = Dog("Жучка")

print(Cat.count)  # Вывод: 2
print(Dog.count)  # Вывод: 1