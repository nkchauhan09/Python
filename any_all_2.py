def add(*args):
    if all([(type(arg) == int or type(arg) == float) for arg in args]):
        t = 0
        for i in args:
            t = t + i
        return t
    else:
        return "wrong input"
print(add(1, 2, 3, 4, 5)) 
print(add(1, 2, 3, "neeraj", 3.5))