# tableformat.py
#
# Exercise 4.7
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
        raise RuntimeError(f'Unknown format {name}')
    return formatter