def evens(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            yield i
even_nums = evens(20)
for num in even_nums:
    print(num)