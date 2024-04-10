data = [5.4, 6.6, 154.1, True, False, [1,2,3,4], 'nevermore', 8, 10]

""" функц. фильтр отбирает только вещественные числа, а функц. сумм суммирует"""
print(sum(filter(lambda x: isinstance(x, float), data)))

print(sum(filter(lambda x: isinstance(x, int), data))) #неверно выводит результат, т.к суммирует еще True
print(sum(filter(lambda x: isinstance(x, int) and type(x) != bool, data))) # верный результат с учётом строгой проверки