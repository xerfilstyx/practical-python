# pcost.py
#
# Exercise 2.15
import csv, sys

def portfolio_cost(filename):
    """A function to read file from filename(dir) and return the total cost"""
    total = 0
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        header = next(rows)     # skip header string
        for rownum, row in enumerate(rows, start = 1):
            try:
                total += int(row[1]) * float(row[2])
            except ValueError:
                print(f'Row {rownum}: Couldn\'t convert: {row}')
    
    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)