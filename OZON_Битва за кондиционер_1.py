import random

n = int(input("Общее кол-во: "))

for i in range(n):
    m = int(input("Введите количество человек: "))
    temp_interval = [15, 30]
    flag = True
    for elem in range(m):
        temp = input("Введите желаемую температуру: ")
        if '>=' in temp:
            if int(temp[2::]) in range(temp_interval[0], temp_interval[1] + 1):
                temp_interval[0] = int(temp[2::])
            elif int(temp[2::]) > temp_interval[1]:
                flag = False
        elif '<=' in temp:
            if int(temp[2::]) in range(temp_interval[0], temp_interval[1] + 1):
                temp_interval[1] = int(temp[2::])
            elif int(temp[2::]) < temp_interval[0]:
                flag = False

        if flag:
            print(random.randint(temp_interval[0], temp_interval[1]))
        else: print(-1)
    print(' ')