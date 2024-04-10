class NewList:

    def __init__(self, lst=None):
        self.lst = lst[:] if lst and type(lst) == list else []

    def get_list(self):
        return self.lst

    @staticmethod
    def remove_items(l1, l2):
        l1_with_types = [(x, type(x)) for x in l1]
        l2_with_types = [(x, type(x)) for x in l2]

        for x in l2_with_types:
            if x in l1_with_types:
                l1_with_types.remove(x)
        return [x[0] for x in l1_with_types]

    def __sub__(self, other):
        if isinstance(other, (list, NewList)):
            sub = other
            if isinstance(other, NewList):
                sub = other.lst
            return NewList(self.remove_items(self.lst, sub))

    def __rsub__(self, other):
        if isinstance(other, (list, NewList)):
            return NewList(self.remove_items(other, self.lst))