# Composition

class Engine:
    def start(self):
        print("Engine starts")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Car starts")


my_car = Car()
my_car.start()


# Aggregation

class Wheel:
    def inflate(self):
        print("Wheel inflated")

class Bicycle:
    def __init__(self, wheels):
        self.wheels = wheels

wheels = [Wheel(), Wheel()]

bike = Bicycle(wheels)
bike.wheels[0].inflate()


# Association

class Employee:
    def __init__(self, name):
        self.name = name

class Company:
    def __init__(self, employees):
        self.employees = employees

john = Employee("John")
jane = Employee("Jane")

company = Company([john, jane])
print(company.employees[0].name)
