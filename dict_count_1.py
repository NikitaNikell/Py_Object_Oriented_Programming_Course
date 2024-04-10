data = [int(i) for i in iter(input, 'конец')]
dic = dict.fromkeys([50, 100, 500], 0)

for elem in data:
    if elem in dic.keys():
        dic[elem] += 1
    else:
        dic[elem] = 1


[print(f"{item} - {value}") for item, value in sorted(dic.items())]


"""
Input:
100
50
500
100
100
конец
"""