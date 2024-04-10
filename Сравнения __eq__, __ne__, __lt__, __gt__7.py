class Body:

    def __init__(self, name: str, ro: (int, float), volume: (int, float)):
        self.name = name
        self.ro = ro
        self.volume = volume

    def mass(self):
        return self.ro * self.volume

    @staticmethod
    def check_value(other):
        if isinstance(other, Body):
            return other.mass()
        elif isinstance(other, (int, float)):
            return other
        raise ValueError(f"Введен неверный формат {type(other)}")

    def __eq__(self, other):
        return self.mass() == self.check_value(other)

    def __lt__(self, other):
        return self.mass() < self.check_value(other)

    def __le__(self, other):
        return self.mass() <= self.check_value(other)


body1 = Body('Nikell', 5, 1)
body2 = Body("Black", 5, 1)


print(body1 > body2)  # True, если масса тела body1 больше массы тела body2
print(body1 == body2) # True, если масса тела body1 равна массе тела body2
print(body1 < 10)     # True, если масса тела body1 меньше 10
print(body2 == 5)     # True, если масса тела body2 равна 5