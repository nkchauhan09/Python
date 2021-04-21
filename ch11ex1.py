def to_pow(num, *args):
    if args:
        return [i**num for i in args]
    else:
        return "You haven't entered any args."
nums = [1, 2, 3, 4]
print(to_pow(2, *nums))