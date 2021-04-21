names = ["neeraj", "kumar", "chauhan"]
for pos, name in enumerate(names):
    print(f"{pos} - {name}")

def func(s, l):
    for pos, name in enumerate(l):
        if name == s:
            return pos
    return -1
print(func("kumar", names))
