string = ["abc", "xyz", "uvw"]
def str_rev(l):
    rev = []
    for i in l:
        r = i[::-1]
        rev.append(r)
    return rev
print(str_rev(string))

