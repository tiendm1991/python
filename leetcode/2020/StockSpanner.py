class StockSpanner:

    def __init__(self):
        self.p = []
        self.s = []

    def next(self, price: int) -> int:
        if len(self.p) == 0:
            self.p.append(price)
            self.s.append(0)
            return 1
        if price < self.p[-1]:
            self.p.append(price)
            self.s.append(len(self.p) - 1)
            return 1
        count = 1
        while self.s and self.p[self.s[-1]] <= price:
            t = self.s.pop()
            if self.s:
                count += t - self.s[-1]
            else:
                count += t + 1
        self.p.append(price)
        self.s.append(len(self.p) - 1)
        return count


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
print(obj.next(31))
print(obj.next(41))
print(obj.next(48))
print(obj.next(59))
print(obj.next(79))
print(obj.next(75))
print(obj.next(85))
