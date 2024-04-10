class WordString:

    def __init__(self, string=None):
        self.__string = string

    def __len__(self):
        if self.__string:
            return len(self.__string.split())

    def __call__(self, indx):
        return self.__string.split()[indx]

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, value):
        if isinstance(value, str):
            self.__string = value


words = WordString()
words.string = "Курс по Python ООП    s    "

n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")