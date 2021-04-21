def last_char(n):
    return n[-1]
name = input("Enter your name : ")
lc = last_char(name)
print(f"Last character of {name} is {lc}")

def odd_even(num):
    if num % 2 == 0:
        return "even"
    return "odd"
num = int(input("Enter a number : "))
print(f"Number is {odd_even(num)}")

def is_even(num):
    return num % 2 == 0
print(is_even(num))