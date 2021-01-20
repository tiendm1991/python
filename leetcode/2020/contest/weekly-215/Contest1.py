class OrderedStream:

    def __init__(self, n: int):
        self.n = n-1
        self.a = [None] * n
        self.p = 0

    def insert(self, id: int, value: str):
        self.a[id-1] = value
        print(self.a, self.p)
        ans = []
        while self.p < self.n and self.a[self.p] is not None:
            ans.append(self.a[self.p])
            self.p += 1
        return ans


s = OrderedStream(5)
print(s.insert(3, "c"))
print(s.insert(1, "a"))
print(s.insert(2, "b"))
print(s.insert(5, "e"))
print(s.insert(4, "d"))
