l = [(1, 2), (3, 4), (5, 6), (7, 8)]
l1, l2 = zip(*l)
print(l1)
print(l2)
new_list = []
for pair in zip(l1, l2):
    new_list.append(max(pair))
print(new_list)