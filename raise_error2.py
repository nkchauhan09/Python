class Mobile:
    def __init__(self, name):
        self.name = name
class Mobile_store:
    def __init__(self):
        self.mobiles = []
    def add_mobile(self, new_mobile):
        if isinstance(new_mobile, Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError("new mobile must be object of Mobile class")
mi = Mobile("mi redmi y1")
mi2 = "mi redmi a1"
mob = Mobile_store()
mob.add_mobile(mi)
mobo = mob.mobiles
print(mobo[0].name)
mob.add_mobile(mi2)
print(mob.mobiles)        
