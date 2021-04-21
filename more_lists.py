numbers = list(range(1, 11))
print(numbers)

popped = numbers.pop()
print(popped)
print(numbers)

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 1, 5, 8, 3, 9, 5]
print(num.index(3, 10, 14))

def negative_list(l):
    neg_num = []
    for i in l:
        neg_num.append(-i)
    return neg_num
print(negative_list(num))