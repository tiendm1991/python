import collections


class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10**9 + 7
        if n == 1:
            return 12
        if n == 2:
            return 54
        preResult = 54
        two = 30
        three = 24
        step = 2
        while step < n:
            two = (two * 3 + three * 2) % mod # two = twoPre * 3 + threePre * 2
            three = (preResult * 2) % mod # three = twoPre * 2 + threePre * 2 = preResult * 2
            preResult = (two + three) % mod # update current result of step, result at step = preResult
            step += 1
        return preResult


s = Solution()
print(s.numOfWays(5000))