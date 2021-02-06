# portfolio.py
#
# Exercise 6.14
class Portfolio:
    
    def __init__(self, holdings):
        self._holdings = holdings

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