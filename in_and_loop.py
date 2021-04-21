s = {"a", "b", "c"}

if "a" in s:
    print("present")
else:
    print("not present")

for i in s:
    print(i)

s1 = {1, 2, 3, 4, 5, 6, 7}
s2 = {4, 5, 6, 7, 8, 9, 10}
union = s1 | s2
intersection = s1 & s2
print(union)
print(intersection)