user = {}
user["name"] = input("Enter name here : ")
user["age"] = int(input("Enter age here : "))
user["fav movies"] = (input("Enter fav movies here : ")).split(",")
user["fav songs"] = (input("Enter fav songs here : ")).split(",")
for key, value in user.items():
    print(f"{key} : {value}")