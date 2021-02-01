# pcost.py
#
# Exercise 1.27
total = 0

with open('Data\portfolio.csv', 'rt') as file:
    header = next(file)     # skip header string
    for line in file:
        row = line.split(',')
        # now row is like ['"AA"', '100', '32.20\n']
        total += int(row[1]) * float(row[2].strip('\n'))

print('Total cost', total)