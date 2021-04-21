num1 = [2, 4, 6, 8, 10]
num2 = [1, 2, 3, 4, 5, 6]
print(all([i % 2 == 0 for i in num1]))
print(all([i % 2 == 0 for i in num2]))
print(any([i % 2 == 0 for i in num2]))