class Dimensions:

    def __init__(self, a: (int, float), b: (int, float), c: (int, float)):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, name, value):
        if value <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        else:
            object.__setattr__(self, name, value)

    def __hash__(self):
        return hash((self.a, self.b, self.c))


s_inp = input() # 1 2 3; 4 5 6.78; 1 2 3; 3 1 2.5

lst_dims = [Dimensions(*map(float, i.split())) for i in s_inp.split("; ")]
lst_dims.sort(key=hash) # сортируем по хешу список.

print(lst_dims)




