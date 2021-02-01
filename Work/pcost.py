# pcost.py
#
# Exercise 1.31
def portfolio_cost(filename):
    """A function to read file from filename(dir) and return the total cost"""
    total = 0
    with open(filename, 'rt') as file:
        header = next(file)     # skip header string
        for line in file:
            row = line.split(',')
            # now row is like ['"AA"', '100', '32.20\n']
            try:
                total += int(row[1]) * float(row[2].strip('\n'))
            except ValueError:
                print('Invalid data. Please check your filename.')
    
    return total

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)