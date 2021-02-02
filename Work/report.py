# report.py
#
# Exercise 2.7
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

def read_prices(filename):
    """Read prices.csv and make the dict"""

    prices = {}

    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    
    return prices

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

# total cost of portfolio
total_cost = 0
for s in portfolio:
    total_cost += s['shares'] * s['price']
print('Total cost', total_cost)

# total value of portfolio
total_value = 0
for s in portfolio:
    total_value += s['shares'] * prices[s['name']]
print('Current value', total_value)

print('Profit', total_value - total_cost)