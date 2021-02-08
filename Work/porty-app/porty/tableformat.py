# tableformat.py
#
# Exercise 9.1
class TableFormatter:
    def headings(self, headers):
        """
        테이블의 헤딩을 반환
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        테이블 데이터의 단일 행을 반환
        """
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    """
    테이블을 일반 텍스트 포맷으로 출력
    """
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end = ' ')
        print()
        print(('-' * 10 + ' ') * len(headers))
    
    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end = ' ')
        print()

class CSVTableFormatter(TableFormatter):
    """
    테이블을 CSV 포맷으로 출력
    """
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    """
    테이블을 HTML 포맷으로 출력
    """
    def headings(self, headers):
        print('<tr>', end = '')
        for h in headers:
            print(f'<th>{h}</th>', end = '')
        print('</tr>')
    
    def row(self, rowdata):
        print('<tr>', end = '')
        for d in rowdata:
            print(f'<td>{d}</td>', end = '')
        print('</tr>')

def create_formatter(name):
    """
    사용자가 지정한 포맷에 따라 각기 다른 TableFormatter 클래스로 포매터 인스턴스 생성
    """
    if name == 'txt':
        formatter = TextTableFormatter()
    elif name == 'csv':
        formatter = CSVTableFormatter()
    elif name == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise FormatError('Unknown table format %s' % name)
    return formatter

def print_table(portfolio, columns, formatter):
    """
    임의의 객체로 구성된 리스트(portfolio)에 대하여 사용자가 지정한 어트리뷰트를 보여주는 테이블을 출력
    """
    # formatter.headings는 사용자가 지정한 어트리뷰트(columns)를 받음. 예컨대 columns = ['name', 'shares']
    formatter.headings(columns)
    for i in portfolio:
        # formatter.row는 portfolio 리스트의 각 객체(i)를 재정의한 rowdata를 받음. 객체(i)에 대하여 지정된 어트리뷰트를 통해 얻어진 데이터를 문자열 리스트로 변환
        rowdata = [str(getattr(i, colname)) for colname in columns]
        formatter.row(rowdata)

class FormatError(Exception):
    pass