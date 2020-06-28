import math


class Solution:
    def numSquares2(self, n: int) -> int:
        a = {}
        x = 1
        while x ** 2 <= n:
            a[x ** 2] = 1
            x += 1

        dp = [0 if i == 0 else n for i in range(n + 1)]
        for i in range(1, n + 1):
            for x in a:
                if x > i:
                    break
                dp[i] = min(dp[i], dp[i - x] + 1)
        return dp[n]

    def numSquares(self, n: int) -> int:
        a = {}
        x = 1
        while x ** 2 <= n:
            a[x ** 2] = 1
            x += 1
        l, q = 0, {0}
        while q:
            newQ = set()
            for cur in q:
                for x in a:
                    val = cur + x
                    if val == n:
                        return l + 1
                    else:
                        newQ.add(val)
            l += 1
            q = newQ
        return n


s = Solution()
print(s.numSquares(6616))
