# pcost.py
#
# Exercise 4.4
import report

def portfolio_cost(portfolio):
    """
    report.py의 read_portfolio를 사용하여 filename(portfolio)을 읽어서 그 최종 소비액을 반환하는 함수
    """
    record = report.read_portfolio(portfolio)
    return sum([stock.shares * stock.price for stock in record])

def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Usage: pcost.py portfoliofile')
    print('Total cost:', portfolio_cost(argv[1]))

if __name__ == '__main__':
    import sys
    main(sys.argv)