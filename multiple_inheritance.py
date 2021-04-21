class A:
    def class_a(self):
        return "class A called"
    def hello(self):
        return "hello A"
class B:
    def class_b(self):
        return "class B called"
    def hello(self):
        return "hello B"
class C(A, B):
    pass
obj_c = C()
    print(obj_c.class_a())
    print(obj_c.class_b())
    print(obj_c.hello())
# print(help(C))
print(C.mro())
print(C.__mro__)