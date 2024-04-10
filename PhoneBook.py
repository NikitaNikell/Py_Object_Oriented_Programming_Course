""" Вы создаете телефонную записную книжку. Она определяется классом PhoneBook."""
class PhoneBook:
    def __init__(self):
        self.sp = []

    def add_phone(self, phone):
        self.sp.append(phone)

    def remove_phone(self, indx):
        self.sp.pop(indx)

    def get_phone_list(self):
        return self.sp


class PhoneNumber:
    def __init__(self, number: int, fio: str):
        self.number = number #через проверку
        self.fio = fio

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: int):
        if isinstance(number, int) and len(str(number)) == 11:
            self.__number = number
        else:
            raise ValueError('Phone number incorrect')


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()

for phone in phones:
    print(f'Name: {phone.fio}, Phone Number: {phone.number}')

for i in phones:
    print(i.number, i.fio)