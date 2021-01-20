import heapq


class Solution:
    def kthSmallestPrimeFraction(self, a, k):
        n = len(a)

        class Fraction:
            def __init__(self, x, y):
                self.x = x
                self.y = y

            def __lt__(self, other):
                return a[self.x] * a[other.y] < a[self.y] * a[other.x]

        if k == 1:
            return [a[0], a[-1]]
        row = []
        for i in range(n - 1):
            heapq.heappush(row, Fraction(i, n - 1))
        ans = []
        while k > 0:
            t = heapq.heappop(row)
            ans = [t.x, t.y]
            if t.y > t.x + 1:
                heapq.heappush(row, Fraction(t.x, t.y - 1))
            k -= 1
        return [a[ans[0]], a[ans[1]]]


s = Solution()
print(s.kthSmallestPrimeFraction([1, 2, 3, 5], 3))
