from random import randint
from string import ascii_lowercase, digits, ascii_uppercase

class EmailValidator:
    EMAIL_CHARS = ascii_lowercase + digits + ascii_uppercase + "_.@"
    EMAIL_RANDOM_CHARS = ascii_lowercase + digits + ascii_uppercase + "_"

    def __new__(cls, *args, **kwargs):
        """ запрет на создание экземпляра класса (ЭК)"""
        return None

    def __init__(self, email):
        self.email = email

    @classmethod
    def get_random_email(cls):
        n = randint(4, 30) #генерируем длину первой части емейла
        length = len(cls.EMAIL_RANDOM_CHARS) - 1
        return "".join(cls.EMAIL_RANDOM_CHARS[randint(0, length)] for i in range(n)) + "@gmail.com"


    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False

        if not set(email) < set(cls.EMAIL_CHARS): #проверка на содержание только определенных символов
            return False

        rez = email.split('@')
        if len(rez) != 2: #проверка на количество вхождений @ в эмейле
            return False

        if len(rez[0]) > 100 or len(rez[1]) > 50: #проверка первой части эмейла на длину до 100 символов и второй части до 50 символом
            return False

        if "." not in rez[1]: #проверка на наличие точки во второй части емейла
            return False

        if  email.count("..") > 0: #проверка на вхождение двух точек подряд во второй части эмейла
            return False

        return True

    @staticmethod
    def __is_email_str(email):
        return isinstance(email, str) # type(email) == str




res1 = EmailValidator.check_email("sc_lib@list.ru") # True
res2 = EmailValidator.check_email("sc_lib@list_ru") # False

print(res1)
print(res2)