# pcost.py
#
# Exercise 2.16
import csv, sys

def portfolio_cost(filename):
    """A function to read file from filename(dir) and return the total cost"""
    total_cost = 0
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        header = next(rows)     # skip header string
        for rownum, row in enumerate(rows, start = 1):
            # use zip() to make new record dict
            record = dict(zip(header, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            except ValueError:
                print(f'Row {rownum}: Couldn\'t convert: {row}')
    
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)