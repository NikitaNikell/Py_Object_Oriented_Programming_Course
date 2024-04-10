class Shop:

    def __init__(self, shop_name):
        self.shop_name = shop_name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        if product in self.goods:
            self.goods.remove(product)


class Product:

    _id_name = 1
    attr = {"name": (str, ), "weight": (int, float), "price": (int, float)}

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        self.id = Product._id_name
        Product._id_name += 1

    def __setattr__(self, key, value):
        match key:
            case "name" if not isinstance(value, str):
                raise TypeError("Неверный тип присваиваемых данных.")
            case "weight" | "price" if not isinstance(value, (int, float)):
                raise TypeError("Неверный тип присваиваемых данных.")
            case _:
                super().__setattr__(key, value)

    def __delattr__(self, item):
        if item == "id":
            raise AttributeError("Атрибут id удалять запрещено.")
        else:
            return object.__delattr__(self, item)


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))




del book.id
print(book.__dict__)



# for p in shop.goods:
#     print(f"{p.name}, {p.weight}, {p.price}")







