"""
Вводятся оценки студента в одну строчку через пробел.
Необходимо определить, имеется ли в этом списке хотя бы одна оценка ниже тройки.
Если это так, то вывести на экран строку "отчислен", иначе - "учится".
"""

ball = list(map(int, input().split()))

print("отчислен" if any(map(lambda x: x <= 2, ball)) else "учится")