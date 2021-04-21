num = input("Enter a number of more than one digit : ")
sum = 0
i = 0
while i < len(num.strip()) :
    sum = sum + int(num[i])
    i = i + 1
print(f"sum of digits is {sum}")
