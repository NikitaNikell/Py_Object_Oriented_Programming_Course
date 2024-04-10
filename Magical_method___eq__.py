class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


people_list = [Person("John", 25), Person("Jane", 30), Person("Bob", 35)]

if Person("John", 25) in people_list:
    print("Yes, 'John' is present in the given list.")
else:
    print("No, 'John' is not present in the given list.")