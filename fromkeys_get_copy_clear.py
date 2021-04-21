d = dict.fromkeys(["name", "age",], "unknown")
print(d)
d = dict.fromkeys(("name", "age",), "unknown")
print(d)
d = dict.fromkeys("abc", "unknown")
print(d)
d = dict.fromkeys(range(1, 11), "unknown")
print(d)
d = dict.fromkeys(["name", "age",], ["unknown", "unknown"])
print(d)

di = {
    "name" : "neeraj",
    "age" : 23,
    "course" : "mca"
}
print(di)
print(di.get("name"))
print(di.get("names"))
print(di.get("names", "not found !"))

if d.get("name"):
    print("present")
else:
    print("not present")

if d.get("names"):
    print("present")
else:
    print("not present")

d.clear()
print(d)

d1 = di.copy()
di.popitem()
print(d1)
print(di)
print(d1 is di)

d1 = di
di.popitem()
print(d1)
print(di)
print(d1 is di)

user = {
    "name" : "neeraj",
    "age" : 23,
    "age" : 24
}
print(user)