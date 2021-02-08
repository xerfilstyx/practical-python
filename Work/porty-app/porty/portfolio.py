# portfolio.py
#
# Exercise 9.1
from . import stock, fileparse

class Portfolio:
    
    def __init__(self):
        self._holdings = []
  
    @classmethod
    def from_csv(cls, lines, **opts):
        # 클래스 메서드 from_csv로 파싱된 데이터를 딕셔너리로 변환한 뒤 Stock 객체에 저장하고 객체를 반환
        self = cls()
        portdicts = fileparse.parse_csv(lines, select = ['name', 'shares', 'price'], types = [str, int, float], **opts)

        for d in portdicts:
            self.append(stock.Stock(**d))
        
        return self

    def append(self, holding):
        if not isinstance(holding, stock.Stock):
            raise TypeError('Expected a Stock instance')
        self._holdings.append(holding)

    def __iter__(self):
        return self._holdings.__iter__()

    def __len__(self):
        return len(self._holdings)

    def __getitem__(self, index):
        return self._holdings[index]
    
    def __contains__(self, name):
        # 제너레이터 표현식을 사용
        return any((s.name == name for s in self._holdings))
    
    @property
    def total_cost(self):
        # 제너레이터 표현식을 사용
        return sum(s.cost for s in self._holdings)
    
    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares