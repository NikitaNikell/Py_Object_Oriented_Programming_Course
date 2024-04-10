class AutoClassAttrib(type):
    def __new__(cls, name, bases, cls_dict, **kwargs):
        new_cls = super().__new__(cls, name, bases, cls_dict)
        if kwargs:
            print('Creating class with some extra attributes: ', kwargs)
            for attr_name, attr_value in kwargs.items():
                setattr(new_cls, attr_name, attr_value)
        return new_cls


class Account(metaclass=AutoClassAttrib,
              extra_attrs=[
                  ('account_type', 'debit'),
                  ('city', 'Paris'),
                  ('overdraft', 1000)]
              ):
    pass


print(Account.__dict__)

print('-' * 15)


class Person(object, metaclass=AutoClassAttrib,
             extra_attrs=[
                 ('country', 'Tailand'),
                 ('citizen', True)]
             ):
    def __init__(self, name, age):
        self.name = name
        self.age = age


print(Person.__dict__)


# rez = Person("Nikell", 19)
# print(rez.__dict__)