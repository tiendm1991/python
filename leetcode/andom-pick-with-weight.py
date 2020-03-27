import random
class Solution:

    def __init__(self, w: List[int]):
        self.prefix = [0] * len(w)
        for i in range(len(w)):
            if i == 0:
                self.prefix[0] = w[0]
            else:
                self.prefix[i] = self.prefix[i-1] + w[i]
        
    def pickIndex(self) -> int:
        def findCeil(n, l, r):
            if l == r or self.prefix[l] >=n:
                return l
            m = (l + r) // 2
            if self.prefix[m] >= n:
                return findCeil(n, l, m)
            else:
                return findCeil(n, m+1, r)
        n = random.randint(1, self.prefix[-1])
        return findCeil(n, 0, len(self.prefix) - 1)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
