class Building:

    def __init__(self, floor):
        self.floor = [None for i in range(floor)]

    def __setitem__(self, key, value):
        if 0 <= key < len(self.floor):
            self.floor[key] = value

    def __getitem__(self, item):
        if 0 <= item < len(self.floor):
            return self.floor[item]

    def __delitem__(self, key):
        if 0 <= key < len(self.floor):
            self.floor[key] = None


iron_building = Building(22)  # Создаем здание с 22 этажами
iron_building[0] = 'Reception'
iron_building[1] = 'Oscorp Industries'
iron_building[2] = 'Stark Industries'
print(iron_building[2])
del iron_building[2]
print(iron_building[2])
