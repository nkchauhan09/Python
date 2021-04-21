class Person:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age
    @classmethod
    def from_string(cls, string):
        name, last_name, age = string.split(",")
        return cls(name, last_name,  int(age))
    @staticmethod
    def hello():
        print("static method called")
    def full_name(self):
        return self.name + " " + self.last_name
    def is_18(self):
        return self.age >= 18
p1 = Person.from_string("neeraj, kumar, 23")
p2 = Person.from_string("pramod, chauhan, 25")
print(p1.is_18())
print(p1.full_name())
Person.hello()
