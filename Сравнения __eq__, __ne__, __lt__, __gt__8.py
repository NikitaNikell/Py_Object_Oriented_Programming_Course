class Thing:

    def __init__(self, name: str, mass: (int, float)):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.mass == other.mass

    def __lt__(self, other):
        return self.name.lower() < other.name.lower() and self.mass < other.mass

    def __le__(self, other):
        return self.name.lower() <= other.name.lower() and self.mass <= other.mass


class Box:

    def __init__(self):
        self.dru_box = []

    def add_thing(self, obj):
        if isinstance(obj, Thing):
            self.dru_box.append(obj)

    def get_things(self):
        return self.dru_box

    def __eq__(self, other: 'Box') -> bool:
        count = 0
        for b1 in self.dru_box:
            for b2 in other.dru_box:
                if b1.name == b2.name and b1.mass == b2.mass:
                    count += 1
        if count == len(self.dru_box) and count == len(other.dru_box):
            return True
        else:
            return False


b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2 # True
print(res)
