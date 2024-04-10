""" Вводится строка целых чисел через пробел.
Необходимо определить, являются ли все эти числа четными.
Вывести True, если это так и False - в противном случае.
"""


def func(n):
    return all(map(lambda x: x % 2 == 0, n))


numbers_1 = [2, 4, 6, 8, 22, 56]
numbers_2 = [1, 2, 4, 6, 8, 22]


assert func(numbers_1) == True
assert (func(numbers_2)) == False

print("Good")
