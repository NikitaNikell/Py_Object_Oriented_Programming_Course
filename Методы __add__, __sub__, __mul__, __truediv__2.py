class NewList:

    def __init__(self, lst=None):
        self._lst = lst[:] if lst and type(lst) == list else []

    def get_list(self):
        return self._lst

    def __sub__(self, other):
        if type(other) not in (list, NewList):
            raise AttributeError("Необходимо передать либо list, NewList")
        other_data = other if type(other) == list else other.get_list()
        return NewList(self.__diff_list(self._lst, other_data))

    def __rsub__(self, other):
        if type(other) != list:
            raise AttributeError("Необходимо передать либо list, NewList")
        return NewList(self.__diff_list(other, self._lst))

    @staticmethod
    def __diff_list(lst1, lst2):
        if len(lst2) == 0:
            return lst1
        sub = lst2[:]
        return [x for x in lst1 if not NewList.__is_elem(x, sub)]

    @staticmethod
    def __is_elem(x, sub):
        res = any(map(lambda xx: type(x) == type(xx) and x == xx, sub))
        if res:
            sub.remove(x)
        return res



lst = NewList()
lst1 = NewList([0, 1, -3.4, "abc", True])
lst2 = NewList([1, 0, True])

assert lst1.get_list() == [0, 1, -3.4, "abc", True] and lst.get_list() == [], "метод get_list вернул неверный список"

res1 = lst1 - lst2
res2 = lst1 - [0, True]
res3 = [1, 2, 3, 4.5] - lst2
lst1 -= lst2

assert res1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"
assert res2.get_list() == [1, -3.4, "abc"], "метод get_list вернул неверный список"
assert res3.get_list() == [2, 3, 4.5], "метод get_list вернул неверный список"
assert lst1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"

lst_1 = NewList([1, 0, True, False, 5.0, True, 1, True, -7.87])
lst_2 = NewList([10, True, False, True, 1, 7.87])
res = lst_1 - lst_2
assert res.get_list() == [0, 5.0, 1, True, -7.87], "метод get_list вернул неверный список"

a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
assert res_4.get_list() == [1, 2], "метод get_list вернул неверный список"