from csv import DictReader, DictWriter
with open("read_csv.csv", "r") as rf:
    with open("write_csv.csv", "w", newline="") as wf:
        csvreader = DictReader(rf)
        csvwriter = DictWriter(wf, fieldnames=["fname","lname","age"])
        csvwriter.writeheader()
        for row in csvreader:
            f_name, l_name, age = row["firstname"],row["lastname"],row["age"]
            csvwriter.writerow({
                "fname":f_name.upper(),
                "lname":l_name.upper(),
                "age":age
            })