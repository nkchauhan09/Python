from csv import writer
with open("csv_file.csv", "w", newline = "") as f:
    write_csv = writer(f)
    write_csv.writerow(["Name","Country"])
    write_csv.writerow(["Neeraj","India"])
    write_csv.writerow(["John","America"])
    write_csv.writerows([["Name","Country"],["Neeraj","India"],["John","America"]])