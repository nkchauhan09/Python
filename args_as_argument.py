def mul(*args):
    print(args)
    m = 1
    for i in args:
        m = m * i
    return m
mlt = [1, 2, 3, 4]
print(mul(*mlt))