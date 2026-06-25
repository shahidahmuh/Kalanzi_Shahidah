#Protected Salary
"""
class Employee:
    def __init__(self):
        self.__salary = 10000
emp = Employee()

print(emp.__salary)
"""

#Exercise create a class called car with brand model price then make brand public model protected and price private
#display all values appropriately

class Car:
    def __init__(self,brand,price,model):
        self.brand = "RollsRoyce"
        self._price =100000
        self.__model = "model"
    def car_details(self):
        print("Car Name: ")

car = Car("RollsRoyce", 10000, "Phantom4")
        
print(car.brand)
print(car.car_details())
