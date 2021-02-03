# pcost.py
#
# Exercise 3.14
import sys, report

def portfolio_cost(filename):
    """A function to read file from filename(dir) and return the total cost"""
    total_cost = 0
    record = report.read_portfolio(filename)
    return sum([stock['shares'] * stock['price'] for stock in record])

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)