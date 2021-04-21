num = list(range(1, 11))
def rev(l):
    rev_list = []
    for i in range(len(l)):
        last = l.pop()
        rev_list.append(last)
    return rev_list
print(rev(num))