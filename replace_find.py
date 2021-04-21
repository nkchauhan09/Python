string = "my name is Neeraj and my age is 23"
print(string.replace("Neeraj", "Neeraj Kumar"))
print(string.replace("my", "his", 2))
print(string.find("is"))
print(string.find("is", 10))
is_pos1 = string.find("is")
is_pos2 = string.find("is", is_pos1 + 1)
print(is_pos2)