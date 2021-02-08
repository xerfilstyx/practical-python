# ticker.py
#
# Exercise 9.1
from .follow import follow
import csv
from . import report

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

# 제너레이터 표현식으로 제너레이터 함수를 대체

def ticker(portfile, logfile, fmt = 'txt'):
    """
    포트폴리오 파일(portfile), 로그 파일(logfile), 포맷(fmt) 형식을 이용해 실시간 주식 티커를 생성하는 함수
    """
    portfolio = report.read_portfolio(portfile)
    rows = parse_stock_data(follow(logfile))
    rows = (row for row in rows if row['name'] in portfolio)
    formatter = report.tableformat.create_formatter(fmt)
    formatter.headings(['Name', 'Price', 'Change'])
    for row in rows:
        rowdata = [row['name'], str(row['price']), str(row['change'])]
        formatter.row(rowdata)

def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: ticker portfoliofile logfile fmt')
    ticker(args[1], args[2], args[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)