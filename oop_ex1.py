class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.name = brand + " " + model
l1 = Laptop("dell", "n5010", 45000)
l2 = Laptop("lenovo", "l3451", 30000)
print(l1.brand)
print(l2.brand)
print(l1.name)