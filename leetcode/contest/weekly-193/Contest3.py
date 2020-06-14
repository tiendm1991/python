class Solution:
    def minDays(self, bloomDay, m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m * k:
            return -1
        _max = max(bloomDay)
        def check(a):
            count = 0
            start = -1
            a += [False]
            for i, v in enumerate(a):
                if not v:
                    start = i
                if i - start == k:
                    count += 1
                    start = i
            return count >= m
        def biSearch(low, high):
            if low > high:
                return -1
            if check([low >= bloom for bloom in bloomDay]):
                return low
            mid = (low + high) // 2
            if check([mid >= bloom for bloom in bloomDay]):
                return biSearch(low, mid)
            else:
                return biSearch(mid + 1, high)
        return biSearch(1, _max)

s = Solution()
print(s.minDays([1000000000,1000000000], 1, 1))