name, char = input("Enter name and character here : ").split(",")
print(f"Name length is {len(name)}")
print(f"Name length is {len(name.strip())}")
print(f"Character count : {name.count(char.upper())+name.count(char.lower())}")
print(f"Character count : {name.lower().count(char.lower())}")
print(f"Character count : {name.strip().count(char.strip().upper())+name.strip().count(char.strip().lower())}")
print(f"Character count : {name.strip().lower().count(char.strip().lower())}")