user_info = {
    "name" : "neeraj",
    "age" : 23,
    "fav movies" : ["uri", "3 idiots"],
    "fav songs" : ["jaane na dunga kahin", "shayad"]
}
if "name" in user_info:
    print("present")
else:
    print("not present")

if "neeraj" in user_info.values():
    print("present")
else:
    print("not present")

if ["uri", "3 idiots"] in user_info.values():
    print("present")
else:
    print("not present")

for i in user_info:
    print(i)

for i in user_info:
    print(user_info[i])

for i in user_info.values():
    print(i)

user_values = user_info.values()
print(user_values) 
print(type(user_values))

user_keys = user_info.keys()
print(user_keys) 
print(type(user_keys))

user_items = user_info.items()
print(user_items)
print(type(user_items))

for i, j in user_items:
    print(f"key is {i} and value is {j}")