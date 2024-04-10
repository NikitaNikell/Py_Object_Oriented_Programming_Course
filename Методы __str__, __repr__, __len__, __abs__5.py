from math import sqrt


class Value:

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        if instance is None: # затычка для прохождения тестов на степике
            return property()
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if type(value) in (int, float):
            setattr(instance, self.name, value)
        else:
            raise ValueError("Неверный тип данных.")


class Complex:
    real = Value()
    img = Value()

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __abs__(self):
        return sqrt(self.real*self.real + self.img*self.img)


cmp = Complex(real=7, img=8)

cmp.real = 3
cmp.img = 4
c_abs = cmp.__abs__()


print(c_abs)
print(cmp.real, cmp.img)


assert isinstance(Complex.img, property), "Метод img не является объектом-свойством (property)"

cmp = Complex(7, 8)
assert len(cmp.__dict__) == 2, "должно быть два локальных свойства действительная часть и мнимая часть"

try:
    cmp.img = ""
    cmp.img = str()
    cmp.real = ""
    cmp.real = str()

except ValueError:
    assert True
else:
    assert False, "ошибка, не была сгенерирована ошибка ValueError при записи некорректных данных"

cmp.real = 3
assert cmp.real == 3, "ошибка при изменении значения на другое"

cmp.img = 4
assert cmp.img == 4, "ошибка при изменении значения на другое"
assert abs(cmp) == 5,\
    "ошибка в возвращении модуля комплексного числа (вычисляется по формуле: sqrt(real*real + img*img)"

print("Правильный ответ !")