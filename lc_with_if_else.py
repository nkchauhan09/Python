list1 = list(range(1, 11))
list2 = []
for i in list1:
    if i % 2 == 0:
        list2.append(i*2)
    else:
        list2.append(-i)
print(list2)

list3 = [i*2 if(i % 2 == 0) else -i for i in list1]
print(list3)
