#!/usr/bin/env python
import csv


data = open("airbus_tree.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []

for rows in csvreader:
	rows.append(rows)

print(rows)
file.close()