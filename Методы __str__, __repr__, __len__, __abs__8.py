class Value:

    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):  # дескрипторы с проверкой
        if self.name in ("__name", "__measure"):
            if not isinstance(value, str):
                raise ValueError(f"Invalid data type {self.name.upper()}")
        elif self.name == "__volume":
            if not isinstance(value, (int, float)):
                raise ValueError(f"Invalid data type {self.name.upper()}")

        setattr(instance, self.name, value)


class Recipe:

    def __init__(self, *args):
        self.ingredient = list(args)

    def add_ingredient(self, ing):
        self.ingredient.append(ing)

    def remove_ingredient(self, ing):
        self.ingredient.remove(ing)

    def get_ingredients(self):
        return tuple(self.ingredient)

    def __len__(self):
        return len(self.ingredient)


class Ingredient:
    name = Value()
    volume = Value()
    measure = Value()

    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f'{self.name}: {self.volume}, {self.measure}'


# ing = Ingredient("Соль", 1, "столовая ложка")
# s = str(ing)  # Соль: 1, столовая ложка
#
# print(s)

recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()


n = len(recipe) # n = 3

i1 = Ingredient("Соль", 1, "столовая ложка")
i2 = Ingredient("Мука", 1, "кг")
i3 = Ingredient("Мясо баранины", 10, "кг")
i4 = Ingredient("Масло", 100, "гр")
recipe = Recipe(i1, i2, i3)
recipe.add_ingredient(i4)
recipe.remove_ingredient(i3)

assert len(recipe) == 3, "функция len вернула неверное значение"
lst = recipe.get_ingredients()
for x in lst:
    assert isinstance(x, Ingredient), "в списке рецептов должны быть только объекты класса Ingredient"
    assert hasattr(x, 'name') and hasattr(x, 'volume') and hasattr(x, 'measure'), "объект класса Ingredient должен иметь атрибуты: name, volume, measure"

assert str(i4) == "Масло: 100, гр", "метод __str__ вернул неверное значение"


i4 = Ingredient("Масло", 120, "гр")
recipe.add_ingredient(i4)
assert len(recipe) == 4, "функция len вернула неверное значение"
