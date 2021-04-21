from csv import DictWriter
with open("write_csv.csv", "w", newline="") as f:
    write_csv = DictWriter(f,fieldnames=["fname","lname","age"])
    write_csv.writeheader()
    write_csv.writerow({
        "fname":"Neeraj",
        "lname":"chauhan",
        "age":23
    })
    write_csv.writerow({
        "fname":"Pramod",
        "lname":"chauhan",
        "age":25
    })
    write_csv.writerows([
        {"fname":"Neeraj","lname":"chauhan","age":23},
    {"fname":"Pramod","lname":"chauhan","age":25}
    ])