mixed = [1, 2, 3, [4, 5], 6, 7, [8, 9], 10, 11, [12, 13]]
def list_count(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count
print(list_count(mixed))
