number = input().replace(" ", "")
print(number)
if number[0] == "+" and number[1] == '7' and len(number) == 11:
    print("Телефон сохранен")
elif number[0] == "8" and number[1] == '9' and len(number) == 11:
    print("Телефон сохранен")
else:
    print('Номер телефона некорректный')



