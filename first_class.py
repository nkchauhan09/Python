class Person:
    def __init__(self, f_name, l_name, age):
        print("init function called")
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
p1 = Person("Neeraj", "Kumar", 23)
p2 = Person("Pramod", "Kumar", 25)
print(p1.f_name)
print(p2.f_name)