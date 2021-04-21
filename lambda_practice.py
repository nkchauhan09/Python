is_even = lambda a : a % 2 == 0
print(is_even(4))
print(is_even(5))
last_char = lambda s : s[-1]
print(last_char("Neeraj"))
is_greater = lambda s : True if len(s) > 5 else False # or lambda s : len(s) > 5
print(is_greater("Neeraj"))
print(is_greater("Kumar"))