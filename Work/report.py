# report.py
#
# Exercise 2.10
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

def make_report(portfolio, prices):
    """Read portfolio list and prices dict and make the list of tuples containing Name, Shares, Prices and Change"""

    report = []

    for s in portfolio:
        holding = (s['name'], s['shares'], prices[s['name']], prices[s['name']] - s['price'])
        report.append(holding)
    
    for r in report:
        print('%10s %10d %10.2f %10.2f' % r)