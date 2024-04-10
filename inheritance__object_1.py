# Напишите реализацию класс NewInt
class NewInt(int):

    def repeat(self, n=2):
        return int(str(self) * n)

    def to_bin(self):
        return int(f'{self:b}')


# Ниже представлены проверки для класса NewInt, не удаляйте этот код

c1 = NewInt(9)
assert isinstance(c1, NewInt)
assert issubclass(NewInt, int)
assert c1 + 9 == 18
assert c1 * 9 == 81

c2 = NewInt(31)
assert c2.repeat() == 3131
assert c2.repeat(4) == 31313131
assert NewInt(16).to_bin() == 10000
assert NewInt(14).to_bin() == 1110

a = NewInt(9)
print(a.repeat())  # печатает число 99
d = NewInt(a + 5)
print(d.repeat(3)) # печатает число 141414
b = NewInt(NewInt(7) * NewInt(5))
print(b.to_bin()) # печатает 100011 - двоичное представление числа 35

# Кстати, как вы думаете, что вернет данный вызов NewInt() ?


print('Good')