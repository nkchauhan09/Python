num = list(range(1, 11))
def odd_even(l):
    odd = []
    even = []
    for i in l:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    filter = [odd, even]
    return filter
print(odd_even(num))