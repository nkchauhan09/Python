mixed = (1,2, 3, 4.0)
# loop in tuple
for i in mixed:
    print(i)

print("\n")

i = 0
while i < len(mixed):
    print(mixed[i])
    i += 1

print("\n")
# one element tuple
num = (1)
num1 = (1, )
print(type(num))
print(type(num1))

print("\n")
# tuple without parenthesis
name = "neeraj", "kumar", "chauhan"
print(type(name))

print("\n")
# tuple unpacking
fname, mname, lname = (name)
print(fname)
print(mname)
print(lname)

print("\n")
# list inside tuple
name = ("name", "is", ["neeraj", "kumar"])
name[2].pop()
name[2].append("chauhan")
print(name)

print("\n")
# functions
print(min(mixed))
print(max(mixed))
print(sum(mixed))