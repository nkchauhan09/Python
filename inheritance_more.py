class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = max(price, 0)
    def name(self):
        return f"{self.brand} {self.model}"
    def call(self, number):
        return(f"calling {number}")
class Smartphone(Phone):
    def __init__(self, brand, model, price, ram, rom, camera):
        super().__init__(brand, model, price)
        self.ram = ram
        self.rom = rom
        self.camera = camera
class Smartphone2(Phone):
    def __init__(self, brand, model, price, ram, rom, camera):
        super().__init__(brand, model, price)
        self.ram = ram
        self.rom = rom
        self.camera = camera
    def name(self):
        return f"{self.brand} {self.model} and price is {self.price}"
class Flagship_phone(Smartphone):
    def __init__(self, brand, model, price, ram, rom, camera, front_cam):
        super().__init__(brand, model, price, ram, rom, camera)
        self.front_cam = front_cam
    def name(self):
        return f"{self.brand} {self.model} and front camera is {self.front_cam}"
smartphone = Smartphone2("mi", "redmi y1", 12000, "4gb", "64gb", "13mp")
flag = Flagship_phone("mi", "redmi a2", 15000, "4gb", "128gb", "16mp", "13mp")
print(smartphone.name())
print(flag.name())
# print(help(Flagship_phone))
print(Flagship_phone.mro())
print(isinstance(smartphone, Smartphone2))
print(isinstance(smartphone, Phone))
print(isinstance(smartphone, Flagship_phone))
print(issubclass(Smartphone, Phone))
print(issubclass(Smartphone2, Phone))
print(issubclass(Flagship_phone, Phone))