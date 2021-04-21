user_info = {
    "name" : "neeraj",
    "age" : 23,
    "fav movies" : ["uri", "3 idiots"]
}
print(user_info)

user_info["fav songs"] = ["jaane na dunga kahin", "shayad"]
user_info["mid name"] = "kumar"
print(user_info)

popped_item = user_info.pop("fav movies")
print(popped_item)
print(type(popped_item))
print(user_info)

pop_item = user_info.popitem()
print(pop_item)
print(type(pop_item))
print(user_info)