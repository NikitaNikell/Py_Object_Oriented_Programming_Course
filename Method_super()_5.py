class Doctor:
    def graduate(self):
        print('Ура, я отучился на доктора')


class Builder:
    def graduate(self):
        print('Ура, я отучился на строителя')


class Person(Builder, Doctor, ):
    def graduate(self):
        print('Посмотрим кем я стал')
        super().graduate()
        Doctor.graduate(self)


print(Person.__mro__)
print()

s = Person()
s.graduate()

