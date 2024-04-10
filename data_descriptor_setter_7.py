class Thing:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Bag:

    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.__things = []

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        s = self.get_total_weight()
        if s + thing.weight <= self.max_weight:
            self.__things.append(thing)

    def remove_thing(self, indx):
        self.__things.pop(indx)

    def get_total_weight(self):
        return sum(i.weight for i in self.__things)


bag = Bag(1000)

bag.add_thing(Thing("Гиря", 1001))

bag.add_thing(Thing("Книга по Python", 100))

bag.add_thing(Thing("Котелок", 500))

bag.add_thing(Thing("Спички", 20))

bag.add_thing(Thing("Бумага", 100))

bag.add_thing(Thing("Гиря", 1001))

w = bag.get_total_weight()

print(w)

for t in bag.things:
    print(f"{t.name}: {t.weight}")