def my_map(func, l):
    return [func(item) for item in l]
print(my_map(lambda a : a**3, [1, 2, 3, 4]))