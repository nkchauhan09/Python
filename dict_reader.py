from csv import DictReader
with open("file.csv", "r") as f:
    dict_reader = DictReader(f, delimiter = ",")
    for row in dict_reader:
        print(row)
        print(row["name"])
        print(row["email"])
        print(row["phone"])