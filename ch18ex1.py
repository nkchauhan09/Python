with open("ch18ex1.txt", "r") as rf:
    with open("ch18ex1a.txt", "a") as wf:
        for line in rf.readlines():
            name, salary = line.split(",")
            wf.write(f"{name}\'s salary is {salary}")
