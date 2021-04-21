with open("file.txt", "w") as f:
    f.write("hello\n")
with open("file.txt", "a") as f:
    f.write("I'm Neeraj\n")
with open("file.txt", "r+") as f:
    f.seek(len(f.read()))
    f.write("\nI'm a student")