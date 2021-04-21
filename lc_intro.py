sqr = []
for i in range(1, 11):
    sqr.append(i**2)
print(sqr)
sqr1 = [i**2 for i in range(1, 11)]
print(sqr1)

neg = []
for j in range(1, 11):
    neg.append(-j)
print(neg)
neg1 = [-j for j in range(1, 11)]
print(neg1)

names = ["neeraj", "kumar", "chauhan"]
first = []
for name in names:
    first.append(name[0])
print(first)
first1 = [name[0] for name in names]
print(first1)