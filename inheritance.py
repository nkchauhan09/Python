class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = max(price, 0)
    def name(self):
        return f"{self.brand} {self.model}"
    def make_call(self, mob_num):
        return f"calling {mob_num}"

class Smartphone(Phone):
    def __init__(self, brand, model, price, ram, rom, camera):
        # Phone.__init__(self, brand, model, price)
        super().__init__(brand, model, price)
        self.ram = ram
        self.rom = rom
        self.camera = camera
phone = Phone("nokia", "1100", 1000)
smartphone = Smartphone("mi", "redmi y1", 12000, "4gb", "64gb", "13mp")
print(phone.name())
print(smartphone.name() + f" price is {smartphone.price}")