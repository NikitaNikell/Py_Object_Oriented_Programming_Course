class Employee:
    __slots__ = ['name', 'age', 'salary']

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


class Manager(Employee):
    __slots__ = ['employees']

    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)



manager = Manager('John Doe', 35, 50000)
employee1 = Employee('Alice Smith', 25, 30000)
employee2 = Employee('Bob Johnson', 30, 40000)
manager.add_employee(employee1)
manager.add_employee(employee2)
print(manager.name)
print(manager.salary)
print(len(manager.employees))

# распаковка __main__.Employee
for i in range(len(manager.employees)):
    print(f"{manager.employees[i]} содержит: name: {manager.employees[i].name}, age: {manager.employees[i].age}, salary: {manager.employees[i].salary}")