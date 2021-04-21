nums = list(range(1, 11))
even = []
for num in nums:
    if num % 2 == 0:
        even.append(num)
print(even)

even1 = [num for num in nums if num % 2 == 0]
even2 = [num for num in range(1, 11) if num % 2 == 0]
odd = [num for num in nums if num % 2 != 0]
print(even1)
print(even2)
print(odd)