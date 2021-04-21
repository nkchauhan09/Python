class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):    
        raise NotImplementedError("declare this function in subclasses")
class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed
class Cat(Animal):
    def __init__(self, name, breed):
        self.breed = breed
doggy = Dog("django", "lebra")
print(doggy.sound())