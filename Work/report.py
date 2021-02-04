# report.py
#
# Exercise 4.6
import fileparse
from stock import Stock
import tableformat

def read_portfolio(portfolio):
    """
    fileparse의 parse_csv를 이용하여 filename(portfolio).csv 파일을 읽고 딕셔너리를 요소로 하는 리스트를 생성
    """
    with open(portfolio, 'rt') as file:
        portdicts = fileparse.parse_csv(file, select = ['name', 'shares', 'price'], types = [str, int, float])
    
    portfolio = [Stock(d['name'], d['shares'], d['price']) for d in portdicts]

    return portfolio

def read_prices(prices):
    """
    fileparse의 parse_csv를 이용하여 filename(prices).csv 파일을 읽고 딕셔너리를 생성
    """
    # 헤더가 없는 경우 parse_csv는 튜플을 요소로 하는 리스트를 반환하므로 이를 딕셔너리로 변환해야 함
    with open(prices, 'rt') as file:
        prices = dict(fileparse.parse_csv(file, types = [str, float], has_headers = False))

    return prices

def make_report(portfolio, prices):
    """Read portfolio class list and prices dict and return the list of tuples containing Name, Shares, Prices and Change"""

    report = []

    for stock in portfolio:
        current_price = prices[stock.name]
        change = current_price - stock.price
        summary = (stock.name, stock.shares, current_price, change)
        report.append(summary)

    return report

def print_report(report, formatter):
    """
    headers 튜플과 make_report로 생성된 report 리스트를 이용하여 보기 좋게 포맷팅된 테이블을 출력
    """
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)

def portfolio_report(portfolio_filename, prices_filename):
    """
    주어진 포트폴리오와 가격 데이터 파일로 주식 보고서를 작성
    """
    # 데이터 파일 읽기
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    # 보고서 데이터 생성
    report = make_report(portfolio, prices)
    # 출력. (Text, CSV, HTML)TableFormatter
    formatter = tableformat.HTMLTableFormatter()
    print_report(report, formatter)

def main(argv):
    if len(argv) != 3:
        raise SystemExit(f'Usage: report.py portfoliofile pricefile')
    portfolio_report(argv[1], argv[2])

if __name__ == '__main__':  # 스크립트가 메인으로 호출된 때에만 실행
    import sys
    main(sys.argv)  # main() 호출. sys.argv는 명령행 인자(command line args)인 텍스트 문자열의 리스트임