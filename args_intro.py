def all_total(*args):
    print(type(args))
    total = 0
    for num in args:
        total += num
    return total
print(all_total(1, 2, 3, 4))