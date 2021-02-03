# report.py
#
# Exercise 3.15
import fileparse

def read_portfolio(portfolio):
    """
    fileparse의 parse_csv를 이용하여 filename(portfolio).csv 파일을 읽고 딕셔너리를 요소로 하는 리스트를 생성
    """
    return fileparse.parse_csv(portfolio)

def read_prices(prices):
    """
    fileparse의 parse_csv를 이용하여 filename(prices).csv 파일을 읽고 딕셔너리를 생성
    """
    # 헤더가 없는 경우 parse_csv는 튜플을 요소로 하는 리스트를 반환하므로 이를 딕셔너리로 변환해야 함
    return dict(fileparse.parse_csv(prices, types = [str, float], has_headers = False))

def make_report(portfolio, prices):
    """Read portfolio list and prices dict and return the list of tuples containing Name, Shares, Prices and Change"""

    report = []

    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        report.append(summary)
    return report

def print_report(report):

    headers = ('Name', 'Shares', 'Price', 'Change')
    
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for r in report:
        print('%10s %10d %10.2f %10.2f' % r)

def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)

def main(argv):
    if len(argv) != 3:
        raise SystemExit(f'Usage: report.py portfoliofile pricefile')
    portfolio_report(argv[1], argv[2])

if __name__ == '__main__':  # 스크립트가 메인으로 호출된 때에만 실행
    import sys
    main(sys.argv)  # main() 호출. sys.argv는 명령행 인자(command line args)인 텍스트 문자열의 리스트임