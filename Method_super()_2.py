class Vehicle:

    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

    def display(self):
        return print(f"Total {self.name} fare is: {self.fare()}")


class Bus(Vehicle):

    def __init__(self, name, mileage, capacity = 50):
        super().__init__(name, mileage, capacity)
        self.capacity = capacity

    def fare(self):
        return super().fare() / 100 * 10 + super().fare()


class Taxi(Vehicle):

    def __init__(self, name, mileage, capacity = 4):
        super().__init__(name, mileage, capacity)
        self.capacity = capacity

    def fare(self):
        return super().fare() / 100 * 35 + super().fare()


sc = Vehicle('Scooter', 100, 2)
sc.display()

merc = Bus("Mercedes", 120000)
merc.display()

polo = Taxi("Volkswagen Polo", 15000)
polo.display()

t = Taxi('x', 111)
assert t.__dict__ == {'name': 'x', 'mileage': 111, 'capacity': 4}
t.display()
b = Bus('t', 123)
assert b.__dict__ == {'name': 't', 'mileage': 123, 'capacity': 50}
b.display()
