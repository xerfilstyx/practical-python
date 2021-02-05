# stock.py
#
# Exercise 4.9
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
    
    def cost(self):
        return self.shares * self.price
    
    def sell(self, sell):
        self.shares -= sell

class MyStock(Stock):
    def __init__(self, name, shares, price, factor):
        # super()의 __init__ 호출
        super().__init__(name, shares, price)
        self.factor = factor

    def panic(self):
        self.sell(self.shares)
    
    def cost(self):
        return self.factor * super().cost()
