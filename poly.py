class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def name(self):
        return f"{self.brand} {self.model}"
    def __str__(self):
        return f"{self.brand} {self.model} and price is {self.price}"
    def __repr__(self):
        return f"Phone(\"{self.brand}\", \"{self.model}\", {self.price})"
    def __len__(self):
        return len(self.name())
    def __add__(self, other):
        return self.price + other.price
phone = Phone("mi", "redmi y1", 12000)
phone2 = Phone("mi", "redmi a1", 15000)
print(phone.__str__())
print(phone.__repr__())
print(len(phone))
print(phone + phone2)