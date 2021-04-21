class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.name = brand + " " + model
    def discount(self, disc):
        # self.disc = disc
        return self.price - (disc / 100) * self.price
l1 = Laptop("dell", "inpiron n5010", 45000)
l2 = Laptop("hp", "bolt 30", 40000)
print(l1.discount(40))
print(l2.discount(25))