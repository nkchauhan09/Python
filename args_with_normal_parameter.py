def multiply(num, *args):
    print(num)
    print(args)
    mul = 1
    for i in args:
        mul *= i
    return mul
print(multiply(4, 3, 2, 1))