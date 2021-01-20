class RLEIterator:

    def __init__(self, a):
        self.a = a
        self.p = 0
        self.v = 0

    def next(self, n: int) -> int:
        if self.p == len(self.a):
            return -1
        self.v += n
        while self.p < len(self.a) and self.v > self.a[self.p]:
            self.v -= self.a[self.p]
            self.p += 2
        if self.p == len(self.a):
            return -1
        return self.a[self.p + 1]


# Your RLEIterator object will be instantiated and called as such:
obj = RLEIterator([3, 8, 0, 9, 2, 5])
print(obj.next(2))
print(obj.next(1))
print(obj.next(1))
print(obj.next(2))
