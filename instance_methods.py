class Person:
    def __init__(self, f_name, l_name, age):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
    def name(self):
        return f"{self.f_name} {self.l_name}"
    def is_18(self):
        return self.age>=18 
p1 = Person("Neeraj", "Kumar", 23)
print(p1.name())
print(p1.is_18())