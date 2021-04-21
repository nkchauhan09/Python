class Circle:
    pi = 3.14
    def __init__(self, rad):
        self.rad = rad
    def area(self):
        return Circle.pi * (self.rad**2)
    def circumference(self):
        return 2 * Circle.pi * self.rad
c1 = Circle(4)
c2 = Circle(5)
print(c1.area())
print(c1.circumference())
print(c2.area())
print(c2.circumference())