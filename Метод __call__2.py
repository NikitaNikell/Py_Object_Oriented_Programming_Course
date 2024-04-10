import random


class RandomPassword:

    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars  # строка из разрешенных в пароле символов
        self.min_length = min_length  # максимальная длина пароля
        self.max_length = max_length  # минимальная длина пароля

    def __call__(self, *args, **kwargs):
        le = random.randint(self.min_length, self.max_length)
        rez = [random.choice(self.psw_chars) for _ in range(le)]
        return ''.join(rez)


rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 10, 20)
lst_pass = [rnd() for _ in range(3)]

print(lst_pass)
