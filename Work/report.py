# report.py
#
# Exercise 3.1
import csv

def read_portfolio(filename):
    """Read portfolio.csv and make the list of dicts"""
    
    portfolio = []

    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        header = next(rows)
        for rownum, row in enumerate(rows, start = 1):
            record = dict(zip(header, row))
            record['shares'] = int(record['shares'])
            record['price'] = float(record['price'])
            portfolio.append(record)
    
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
    """Read portfolio list and prices dict and return the list of tuples containing Name, Shares, Prices and Change"""

    report = []

    for s in portfolio:
        holding = (s['name'], s['shares'], prices[s['name']], prices[s['name']] - s['price'])
        report.append(holding)

    return report

report = make_report(portfolio, prices)

def print_report(report):

    headers = ('Name', 'Shares', 'Price', 'Change')
    
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for r in report:
        print('%10s %10d %10.2f %10.2f' % r)

print_report(report)