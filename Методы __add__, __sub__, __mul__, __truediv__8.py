class MaxPooling:

    def __init__(self, step=(2,2), size=(2,2)):
        self.__step = step
        self.__size = size

    def __call__(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0

        if rows == 0:
            return [[]]

        if not all(map(lambda x: len(x) == cols, matrix)) or \
                not all(map(lambda row: all(map(lambda x: type(x) in (int, float), row)), matrix)):
            raise ValueError
        h, w = self.__size[0], self.__size[1]
        sh, sw = self.__step[0], self.__step[1]

        rows_range = (rows - h) // sh + 1
        cols_range = (cols - w) // sw + 1

        res = [[0] * cols_range for _ in range(rows_range)]

        for i in range(rows_range):
            for j in range(cols_range):
                s = (x for r in matrix[i * sh: i * sh + h] for x in r[j * sw: j * sw + w])
                res[i][j] = max(s)
        return res


mp = MaxPooling(step=(2, 2), size=(2, 2))
m1 = [[1, 10, 10], [5, 10, 0], [0, 1, 2]]
m2 = [[1, 10, 10, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res1 = mp(m1)
res2 = mp(m2)

assert res1 == [[10]], "неверный результат операции MaxPooling"
assert res2 == [[10, 12], [40, 300]], "неверный результат операции MaxPooling"

mp = MaxPooling(step=(3, 3), size=(2, 2))
m3 = [[1, 12, 14, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res3 = mp(m3)
assert res3 == [[12]], "неверный результат операции при MaxPooling(step=(3, 3), size=(2,2))"

try:
    res = mp([[1, 2], [3, 4, 5]])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не прямоугольную матрицу"

try:
    res = mp([[1, 2], [3, '4']])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не числовые значения в матрице"

mp = MaxPooling(step=(1, 1), size=(5, 5))
res = mp([[5, 0, 88, 2, 7, 65],
          [1, 33, 7, 45, 0, 1],
          [54, 8, 2, 38, 22, 7],
          [73, 23, 6, 1, 15, 0],
          [4, 12, 9, 1, 76, 6],
          [0, 15, 10, 8, 11, 78]])  # [[88, 88], [76, 78]]

assert res == [[88, 88], [76, 78]], "неверный результат операции MaxPooling(step=(1, 1), size=(5, 5))"