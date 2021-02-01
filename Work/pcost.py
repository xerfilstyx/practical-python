# pcost.py
#
# Exercise 1.33
import csv, sys

def portfolio_cost(filename):
    """A function to read file from filename(dir) and return the total cost"""
    total = 0
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        header = next(rows)     # skip header string
        for row in rows:
            # now row is like ['AA', '100', '32.20' thanks to csv module]
            try:
                total += int(row[1]) * float(row[2])
            except ValueError:
                print('Invalid data. Please check your filename.')
                break
    
    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)