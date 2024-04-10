
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        obj.prev = self.tail
        if self.tail:
            self.tail.next = obj
        self.tail = obj
        if self.head is None:
            self.head = obj

    def remove_obj(self, indx):
        del_obj = self.get_obj(indx)
        if del_obj is None:
            return
        p, n = del_obj.prev, del_obj.next
        if p:
            p.next = n
        if n:
            n.prev = p

        if self.head == del_obj:
            self.head = n
        if self.tail == del_obj:
            self.tail = p

    def __len__(self):
        check = self.head
        total = 0
        while check:
            check = check.next
            total += 1
        return total

    def __call__(self, indx):
        obj = self.get_obj(indx)
        return obj.data if obj else None

    def get_obj(self, indx):
        check = self.head
        total = 0
        while check and total < indx:
            check = check.next
            total += 1
        return check


class Value:

    def __set_name__(self, owner, name):
        self.name = '_' + owner.__name__ + '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class ObjList:
    data = Value()
    prev = Value()
    next = Value()

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None





ln = LinkedList()
ln.add_obj(ObjList("Сергей"))
ln.add_obj(ObjList("Балакирев"))
ln.add_obj(ObjList("Python ООП"))
ln.remove_obj(2)
assert len(ln) == 2, "функция len вернула неверное число объектов в списке, возможно, неверно работает метод remove_obj()"
ln.add_obj(ObjList("Python"))
assert ln(2) == "Python", "неверное значение атрибута __data, взятое по индексу"
assert len(ln) == 3, "функция len вернула неверное число объектов в списке"
assert ln(1) == "Балакирев", "неверное значение атрибута __data, взятое по индексу"

n = 0
h = ln.head
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__next
    n += 1

assert n == 3, "при перемещении по списку через __next не все объекты перебрались"

n = 0
h = ln.tail
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__prev
    n += 1

assert n == 3, "при перемещении по списку через __prev не все объекты перебрались"



