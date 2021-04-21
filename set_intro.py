s = {1, 2, 3, 4}
print(s)
# removing duplicates
l = [1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 9, 9]
l1 = list(set(l))
print(l1)
s.add(5)
s.add(6)
s.remove(1)
s.remove(2)
s.discard(7)
print(s)
s1 = s.copy()
s.clear()
print(s)
print(s1)
s2 = {1, 2.1, "neeraj"}
print(s2)