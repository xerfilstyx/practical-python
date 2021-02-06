# report.py
#
# Exercise 7.4
import fileparse
from stock import Stock
import tableformat
from portfolio import Portfolio

def read_portfolio(portfolio, **opts):
    """
    fileparse의 parse_csv를 이용하여 filename(portfolio).csv 파일을 읽고 딕셔너리를 요소로 하는 리스트를 생성
    """
    with open(portfolio, 'rt') as file:
        portdicts = fileparse.parse_csv(file, select = ['name', 'shares', 'price'], types = [str, int, float], **opts)
    
    # 딕셔너리 언패킹으로 코드를 단순화
    portfolio = [Stock(**d) for d in portdicts]
    # portfolio에서 임포트한 Portfolio로 인스턴스 생성
    return Portfolio(portfolio)

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
    tableformat 모듈에 정의된 TableFormatter 클래스와 make_report로 생성된 report 리스트를 이용하여 보기 좋게 포맷팅된 테이블을 출력
    """
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)

def portfolio_report(portfolio_filename, prices_filename, fmt = 'txt'):
    """
    주어진 포트폴리오, 가격 데이터 파일, 포맷 지정으로 주식 보고서를 작성
    """
    # 데이터 파일 읽기
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    # 보고서 데이터 생성
    report = make_report(portfolio, prices)
    # 출력. 사용자의 포맷 지정으로 해당 포맷을 적용
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(argv):
    if len(argv) != 4:
        raise SystemExit(f'Usage: report.py portfoliofile pricefile fmt')
    portfolio_report(argv[1], argv[2], argv[3])

if __name__ == '__main__':  # 스크립트가 메인으로 호출된 때에만 실행
    import sys
    main(sys.argv)  # main() 호출. sys.argv는 명령행 인자(command line args)인 텍스트 문자열의 리스트임