def get_list_dig(it):

    """
    Определите функцию с именем get_list_dig, которая возвращает список только
    из числовых значений переданной ей коллекции (список или кортеж).
    """
    return list(filter(lambda x: (isinstance(x, int) or isinstance(x, float)) and type(x) != bool, it))


print(get_list_dig([1 ,2 ,3, "a", True, [4, 5], "c", (4, 5)]))
print(get_list_dig({5, 6, 7, '8', 5, '4'}))
print(get_list_dig((10, "f", '33', True, 12)))
print(get_list_dig(['1', True, False, (1, 23)]))