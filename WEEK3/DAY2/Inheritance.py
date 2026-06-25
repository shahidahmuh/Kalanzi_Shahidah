#Inheriting attributes and methods from another class
class Animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def info(self):
        print("Animal name: ", self.name)
        