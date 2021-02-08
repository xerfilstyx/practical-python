# pcost.py
#
# Exercise 9.1
from . import report

def portfolio_cost(portfolio):
    """
    report.py의 read_portfolio를 사용하여 filename(portfolio)을 읽어서 그 최종 비용(주식 수 * 가격)을 반환하는 함수
    """
    record = report.read_portfolio(portfolio)
    return record.total_cost

def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Usage: pcost.py portfoliofile')
    print('Total cost:', portfolio_cost(argv[1]))

if __name__ == '__main__':
    import sys
    main(sys.argv)