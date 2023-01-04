#!/usr/bin/env python
#import csv
import pandas as pd


pd.options.display.max_rows = 20000 # Allow up to 20,000 rows
file = pd.read_csv("airbus_tree.csv")

sorted_df = file.sort_values(by=["time"], ascending=False)
print(sorted_df)


"""
file = open("airbus_tree.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []

for rows in csvreader:
	rows.append(rows)

print(rows)
file.close()
"""