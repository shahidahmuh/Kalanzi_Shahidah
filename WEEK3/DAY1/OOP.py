#Define a class
class Dog:
    #Define the constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #Define a method
    def bark(self):
        return f"{self.name} says Woof!"
    