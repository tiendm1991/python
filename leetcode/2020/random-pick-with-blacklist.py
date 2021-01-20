import random


class Solution:

    def __init__(self, N, blacklist):
        self.n = N
        blacklist.sort()
        blacklist.append(N)
        self.a = []
        start = 0
        for x in blacklist:
            if start == x:
                start += 1
                continue
            self.a.append([start, x])
            start = x + 1
        self.s = [self.a[0][1] - self.a[0][0]]
        for i in range(1, len(self.a)):
            self.s.append(self.s[-1] + self.a[i][1] - self.a[i][0])
        self.M = self.s[-1]

    def pick(self) -> int:
        def bSearch(l, r, v):
            if self.s[l] >= v:
                return l
            m = (l + r) // 2
            if self.s[m] < v:
                return bSearch(m + 1, r, v)
            else:
                return bSearch(l, m, v)

        x = random.randint(1, self.M)
        i = bSearch(0, len(self.s) - 1, x)
        return random.randrange(self.a[i][0], self.a[i][1])


# Your Solution object will be instantiated and called as such:
obj = Solution(4, [1])
for i in range(10):
    print(obj.pick())
