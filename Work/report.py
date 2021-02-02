# report.py
#
# Exercise 2.5
import csv

def read_portfolio(filename):
    """Read portfolio.csv and make the list of dicts"""
    
    portfolio = []

    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        header = next(rows)
        for row in rows:
            holding = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
                }
            portfolio.append(holding)
    
    return portfolio