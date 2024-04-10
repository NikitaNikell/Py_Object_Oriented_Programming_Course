class DigitRetrieve:

    """ Объявите класс DigitRetrieve для преобразования данных из строки в числа. """

    def __call__(self, num, *args, **kwargs):
        return int(num) if num.isdigit() or num[0] == "-" and num[1:].isdigit() else None



dg = DigitRetrieve()

st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]
print(digits)