fruits1 = ["grapes", "banana", "apple", "mango"]
fruits2 = ("grapes", "banana", "apple", "mango")
fruits3 = {"grapes", "banana", "apple", "mango"}
print(sorted(fruits1))
print(fruits1)
print(sorted(fruits2))
print(fruits2)
print(sorted(fruits3))
print(fruits3)
names = [
    {"name" : "neeraj", "age" : 23},
    {"name" : "kumar", "age" : 22},
    {"name" : "chauhan", "age" : 25}
]
print(sorted(names, key = lambda d : d["age"]))
print(sorted(names, key = lambda d : d["age"], reverse = True))