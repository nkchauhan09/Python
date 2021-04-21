list1 = [1, 2, 3, 4, 5]
list2 = [1, 3, 5, 7, 9]
def common(l1, l2):
    com = []
    for i in l1:
        for j in l2:
            if i == j:
                com.append(i)
    return com
print(common(list1, list2))
