def power(x):
    def num(n):
        return n**x
    return num
cube = power(3)
print(cube(4))
square = power(2)
print(square(3))