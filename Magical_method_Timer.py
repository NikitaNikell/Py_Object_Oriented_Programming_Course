from time import perf_counter


class Timer:
    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        print(f"Вызывается функция или метод: {self.fn.__name__}")
        result = self.fn(*args, **kwargs)
        finish = perf_counter()
        print(f"Функция или метод отработали за {finish - start}")
        return result

# @Timer
# def fact(n):
#     pr = 1
#     for i in range(1, n + 1):
#         pr *= i
#     return pr
#
#
# print(fact(2))

@Timer
def calculate():
    for i in range(10000000):
        2**100

print(calculate())