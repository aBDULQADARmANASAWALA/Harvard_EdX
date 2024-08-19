from tabulate import tabulate
from sys import argv, exit
import csv

if len(argv) != 2 or not argv[1].endswith(".csv"):
    print("Invalid command-line arguments")
    exit(1)

pizza = []
count = 0
with open(argv[1]) as file:
    reader = csv.reader(file)
    for row in reader:
        if count == 0:
            header = row
            count += 1
        else:
            pizza.append(row)

print(tabulate(pizza, header, tablefmt="grid"))
