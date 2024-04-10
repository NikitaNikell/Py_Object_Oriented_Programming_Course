import random

c = int(input("Общее кол-во: "))

requirement_temp = [[input("Введите желаемую температуру: ") for _ in range(int(input("Введите количество человек: ")))] for _ in range(c)]
counter = 0

for items in requirement_temp:
    min_temp, max_temp = 15, 30
    for item in items:
        pointer, value = item.split()

        if pointer == ">=":
            min_temp = int(value)
        elif pointer == "<=":
            max_temp = int(value) if max_temp > int(value) else max_temp

        if min_temp <= max_temp:
            print(random.randint(min_temp, max_temp))
        else:
            print(-1)
    if counter < c-1:
        counter += 1

        print()
    else:
        continue

# 4

# 1
# >= 30

# 6
# >= 18
# <= 23
# >= 20
# <= 27
# <= 21
# >= 28

# 3
# <= 25
# >= 20
# >= 25

# 3
# <= 15
# >= 30
# <= 24