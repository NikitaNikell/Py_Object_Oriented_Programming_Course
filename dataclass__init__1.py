from dataclasses import dataclass

@dataclass
class Customer:
    name: str
    balance: int
    age: int = None



jack = Customer('jack', 500)
print(jack)
print(jack.name, jack.balance, jack.age)


""" Используя dataclass теперь

код становится короче и выразительнее
не нужно определять метод __init__
не нужно определять метод __repr__ и метод __str__
нужно прописывать аннотацию для указания типов атрибутов"""