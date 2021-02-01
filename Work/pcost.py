# pcost.py
#
# Exercise 1.32
import csv

def portfolio_cost(filename):
    """A function to read file from filename(dir) and return the total cost"""
    total = 0
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        header = next(rows)     # skip header string
        for row in rows:
            print(row)
            # now row is like ['AA', '100', '32.20' thanks to csv module]
            try:
                total += int(row[1]) * float(row[2])
            except ValueError:
                print('Invalid data. Please check your filename.')
    
    return total

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)