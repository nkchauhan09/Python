names = ["Neeraj", "Kumar", "Chauhan"]
print(max(names, key = lambda i : len(i)))
print(min(names, key = lambda i : len(i)))
students = {
    "neeraj" : {"score" : 80, "age" : 23},
    "kumar" : {"score" : 70, "age" : 23},
    "chauhan" : {"score" : 90, "age" : 23}
}
students1 = [
    {"name" : "neeraj", "score" : 90, "age" : 23},
    {"name" : "kumar", "score" : 70, "age" : 23},
    {"name" : "chauhan", "score" : 50, "age" : 23}
]
print(max(students1, key = lambda i : i.get("score")))
print(max(students1, key = lambda i : i.get("score"))["name"])
print(max(students, key = lambda i : students[i]["score"]))