# pcost.py
#
# Exercise 5.8
import report

def portfolio_cost(portfolio):
    """
    report.py의 read_portfolio를 사용하여 filename(portfolio)을 읽어서 그 최종 소비액을 반환하는 함수
    """
    record = report.read_portfolio(portfolio)
    return sum([stock.cost for stock in record])    # @property로 stock.cost()가 프로퍼티로 변경된 것을 반영

def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Usage: pcost.py portfoliofile')
    print('Total cost:', portfolio_cost(argv[1]))

if __name__ == '__main__':
    import sys
    main(sys.argv)