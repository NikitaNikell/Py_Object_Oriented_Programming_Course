class Clock:

    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Введен неверный формат данных")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        sec = self.seconds % 60
        minute = (self.seconds // 60) % 60
        hours = (self.seconds // 3600) % 24

        #return f"{self.__get_formatted(hours)}:{self.__get_formatted(minute)}:{self.__get_formatted(sec)}"
        return f'{hours:02d}:{minute:02d}:{sec:02d}'

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0") # для корректного формата вывода времени с 0

    def check(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть целым числом (int) или Clock")
        return True

    def __add__(self, other):
        if self.check(other):
            sc = other
            if isinstance(other, Clock):
                sc = other.seconds
            return __class__(self.seconds + sc)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        if self.check(other):
            sc = other
            if isinstance(other, Clock):
                sc = other.seconds
            self.seconds += sc
            return self


cl1 = Clock(1000)
cl2 = 1000 + cl1
cl1 += 100


print(cl1.get_time())
print(cl2.get_time())

