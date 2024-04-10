class Car:

    def __init__(self, model=""):
        self.__model = model

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if type(value) is str and 2 <= len(value) <= 100:
            self.__model = value


car = Car()
car1 = Car()

car.model = "Toyota"
car1.model = "f"

print(car.model)
print(car1.model)