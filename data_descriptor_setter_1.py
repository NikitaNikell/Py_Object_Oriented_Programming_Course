class Integer:

    @classmethod
    def check(cls, value):
        if type(value) != int:
            raise TypeError("Координата должна быть целым числом")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        #return instance.__dict__[self.name] #АНАЛОГ
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.check(value)
        #instance.__dict__[self.name] = value #АНАЛОГ
        setattr(instance, self.name, value)


class Point3D:

    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p = Point3D(1,2,3)

print(p.__dict__)
print(p.z)

""" 
дескриптор не данных (non-data descriptor), когда в классе присутствует метод __get__, но отсутствует метод __set__
дескриптор данных (data descriptor), когда в классе присутствуют методы __get__ и __set__
"""
