class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self._price = max(price, 0)
    @property
    def complete_specification(self): 
        return f"{self.brand} {self.model} for price {self._price}"
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, new_price):
        self._price = max(new_price, 0)
    def make_call(self, phone_no):
        print(f"calling {phone_no}")
    def name(self):
        print(f"{self.brand} {self.model}")
phone1 = Phone("mi", "redmi y1", 12000)
print(phone1.brand)
print(phone1.model)
phone1.price = -10000
print(phone1.price)
print(phone1.complete_specification)
phone1.name()