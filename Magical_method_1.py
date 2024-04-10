# Напишите определение класса Person
class Person:

    def __init__(self, name, surname, gender="male"):
        self.name = name
        self.surname = surname
        if gender in ["male", "female"]:
            self.gender = gender
        else:
            print("Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
            self.gender = "male"

    def __str__(self):
        return f"Гражданин {self.surname} {self.name}" if self.gender == "male" else f"Гражданка {self.surname} {self.name}"


# Ниже код для проверки методов класса Person
p1 = Person('Chuck', 'Norris')
assert p1.name == 'Chuck'
assert p1.surname == 'Norris'
assert p1.gender == 'male'
assert isinstance(p1, Person)
assert str(p1) == 'Гражданин Norris Chuck'

p2 = Person('Оби-Ван', 'Кеноби', True)  # нужно распечатать предупреждение из условия
assert str(p2) == 'Гражданин Кеноби Оби-Ван'
assert p2.__dict__ == {'name': 'Оби-Ван', 'surname': 'Кеноби', 'gender': 'male'}
assert isinstance(p2, Person)

p3 = Person('Mila', 'Kunis', 'female')
assert isinstance(p3, Person)
assert str(p3) == 'Гражданка Kunis Mila'

print(p1)
print(p2)
print(p3)
