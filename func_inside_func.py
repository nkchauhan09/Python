def bigger(a, b):
    if a > b:
        return a
    return b

def biggest(a, b, c):
    big = bigger(a, b)
    return bigger(big, c)

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
n3 = int(input("Enter third number : "))
bigg = biggest(n1, n2, n3)
print(f"{bigg} is biggest")