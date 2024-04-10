class DigitRetrieve:

    def __init__(self, num=None):
        self.num = num

    def __call__(self, *args, **kwargs):
        try:
            return int(args[0])
        except:
            return None


dg = DigitRetrieve()

st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]
print(digits)
