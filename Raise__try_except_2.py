def first_func():
    print('Начало работы функции first_func')
    try:
        second_func()
    except Exception as ex:
        print(f'Внимание! Обработано исключение: {ex} на уровне first_func')
    print('Конец работы функции first_func')


def second_func():
    print('Начало работы функции second_func')
    try:
        third_func()
    except Exception as ex:
        print(f'Внимание! Обработано исключение: {ex} на уровне second_func')
    print('Конец работы функции second_func')


def third_func():
    print('Начало работы функции third_func')
    try:
        1 / 0
    except Exception as ex:
        print(f'Внимание! Обработано исключение: {ex} на уровне third_func')
    print('Конец работы функции third_func')


print(1)
print(2)
first_func()
print(3)