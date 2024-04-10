class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password

    @staticmethod
    def is_include_digit(password: str):
        return password.isalpha() + password.isdigit()

    @staticmethod
    def is_include_all_register(password: str):
        return password.islower() + password.isupper()

    @staticmethod
    def is_include_only_latin(password):
        for i in password:
            return i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    @staticmethod
    def check_password_dictionary(password):
        return password in open(r'easy_passwords.txt').read()

    @login.setter
    def login(self, value: str):
        if not isinstance(value, str):
            raise TypeError
        elif value.count('@') != 1:
            raise ValueError
        elif '.' not in value[value.find('@'):]:
            raise ValueError
        self.__login = value

    @password.setter
    def password(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Пароль должен быть строкой")
        elif not 4 < len(value) < 12:
            raise ValueError("Пароль должен быть длиннее 4 и меньше 12 символов")
        elif self.is_include_digit(value):
            raise ValueError("Пароль должен содержать хотя бы одну цифру")
        elif self.is_include_all_register(value):
            raise ValueError("Пароль должен содержать хотя бы один символ верхнего и нижнего регистра")
        elif not self.is_include_only_latin(value):
            raise ValueError("Пароль должен содержать только латинский алфавит")
        elif self.check_password_dictionary(value):
            raise ValueError("Ваш пароль содержится в списке самых легких")
        self.__password = value


try:
    s2 = Registration("fga", "asd12")
except ValueError as e:
    pass
else:
    raise ValueError("Registration('fga', 'asd12') как можно записать такой логин?")

try:
    s2 = Registration("fg@a", "asd12")
except ValueError as e:
    pass
else:
    raise ValueError("Registration('fg@a', 'asd12') как можно записать такой логин?")

s2 = Registration("translate@gmail.com", "as1SNdf")
try:
    s2.login = "asdsa12asd."
except ValueError as e:
    pass
else:
    raise ValueError("asdsa12asd как можно записать такой логин?")

try:
    s2.login = "asdsa12@asd"
except ValueError as e:
    pass
else:
    raise ValueError("asdsa12@asd как можно записать такой логин?")

assert Registration.check_password_dictionary('QwerTy123'), 'проверка на пароль в слове не работает'

try:
    s2.password = "QwerTy123"
except ValueError as e:
    pass
else:
    raise ValueError("QwerTy123 хранится в словаре паролей, как его можно было сохранить?")

try:
    s2.password = "KissasSAd1f"
except ValueError as e:
    pass
else:
    raise ValueError("KissasSAd1f хранится в словаре паролей, как его можно было сохранить?")

try:
    s2.password = "124244242"
except ValueError as e:
    pass
else:
    raise ValueError("124244242 пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "RYIWUhjkdbfjfgdsffds"
except ValueError as e:
    pass
else:
    raise ValueError("RYIWUhjkdbfjfgdsffds пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "CaT"
except ValueError as e:
    pass
else:
    raise ValueError("CaT пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "monkey"
except ValueError as e:
    pass
else:
    raise ValueError("monkey пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "QwerTy123"
except ValueError as e:
    pass
else:
    raise ValueError("QwerTy123 пароль есть в слове, нельзя его использовать")

try:
    s2.password = "HelloQEWq"
except ValueError as e:
    pass
else:
    raise ValueError("HelloQEWq пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = [4, 32]
except TypeError as e:
    pass
else:
    raise TypeError("Пароль должен быть строкой")

try:
    s2.password = 123456
except TypeError as e:
    pass
else:
    raise TypeError("Пароль должен быть строкой")

print('U r hacked Pentagon')
