class StripChars:
    """ Функция для форматирования строк и удаления лишних символов"""

    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        """ метод позволяет вызывать объекты класса подобно функциям, в котором определен метод __call__() """
        if not isinstance(args[0], str):
            raise TypeError("Аргумент должен быть строкой")

        return args[0].strip(self.__chars)  # удаление символов с левого и правого конца строки self.__chars

    def __str__(self):
        return self.__chars


s1 = StripChars(" !,#$%^&*(()))")
s2 = StripChars(" 19")

res = s1("!& Hello World!  ")
res1 = s2("1   !Call me! pls! - 123456789   ")

print(res)
print(res1)

print(s1)
print(s2)
