class Person:
    count_instance = 0
    def __init__(self, name, age):
        Person.count_instance += 1
        self.name = name
        self.age = age
    @classmethod
    def count_instances(cls):
        return f"no. of instances are {cls.count_instance} of {cls.__name__} class"
p1 = Person("neeraj", 23)
p2 = Person("pramod", 25)
print(Person.count_instances())