from sys import argv, exit
import csv

if len(argv) != 3 or not argv[1].endswith(".csv"):
    print("Invalid command-line arguments")
    exit(1)

names = []
i = 0
try:
    with open(argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            lname, fname = row["name"].split(", ")
            names.append({"f_name": fname, "l_name": lname, "house": row["house"]})
except FileNotFoundError:
    exit(2)

with open(argv[2], "w") as file:
    writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
    writer.writeheader()
    for name in names:
        writer.writerow({"first": name["f_name"], "last": name["l_name"], "house":name["house"]})
