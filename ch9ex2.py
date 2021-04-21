list1 = [1, 2.0, 3, "neeraj", 4.2, True, False, None, 5]
def num(l):
    return [str(n) for n in l if (type(n) == int or type(n) == float)]
print(num(list1))