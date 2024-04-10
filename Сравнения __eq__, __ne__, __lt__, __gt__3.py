stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]


class StringText:

    def __init__(self, lst_words):
        self.lst_words = list(lst_words)

    def __len__(self):
        return len(self.lst_words)

    def __eq__(self, other):  # == и !=
        return len(self.lst_words) == len(other.lst_words)

    def __lt__(self, other):  # < и >
        return len(self.lst_words) < len(other.lst_words)

    def __le__(self, other):  # <= и >=
        return len(self.lst_words) <= len(other.lst_words)


strip_chars = '–?!,.;'
lst_text = [StringText(x.strip(strip_chars) for x in line.split() if len(x.strip(strip_chars)) > 0) for line in stich]
lst_text_sorted = sorted(lst_text, reverse=True)
lst_text_sorted = [' '.join(x.lst_words) for x in lst_text_sorted]

assert all([[True if i in _ else False for i in "–?!,.;"] for _ in stich]), \
    "в stich есть знаки которые нужно удалить - (–?!,.;)"
assert len(lst_text) == 7 and all(
    True if isinstance(_, StringText) else False for _ in lst_text), "ошибка в lst_text"

assert lst_text_sorted == ['Я к вам пишу чего же боле',
                           'Теперь я знаю в вашей воле',
                           'Но вы к моей несчастной доле',
                           'Что я могу еще сказать',
                           'Хоть каплю жалости храня',
                           'Вы не оставите меня',
                           'Меня презреньем наказать'], "неверно отсортирован список lst_text_sorted"

assert lst_text[0] > lst_text[4] and lst_text[4] > lst_text[1], "метод > работает неверно"
assert lst_text[1] < lst_text[4], "метод < работает неверно"

assert lst_text[2] >= lst_text[4], "метод >= работает неверно"
assert lst_text[2] <= lst_text[4], "метод >= работает неверно"

print("Правильный ответ.")


# stich = list(map(lambda x: list(map(lambda w: w.strip("-?!,.;") if w != '–' else w, x.split())), stich))