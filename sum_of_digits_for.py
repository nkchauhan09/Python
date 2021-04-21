num = input("Enter a number : ")
sum = 0
for i in range (len(num)):
    sum = sum + int(num[i])
print(f"Sum of digits : {sum}")