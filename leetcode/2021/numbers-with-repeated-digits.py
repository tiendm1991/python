import math


class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        def arrangement(a, b):
            return math.factorial(a) // math.factorial(a - b)

        arr = [int(c) for c in str(N)]
        n = len(arr)
        res = 0
        for d in range(1, n):
            res += 9 * arrangement(9, d - 1)
        s = set()
        for i, x in enumerate(arr):
            for y in range(1 if i == 0 else 0, x):
                if y not in s:
                    res += arrangement(9 - len(s), n - 1 - i)
            if x in s:
                break
            s.add(x)
        if len(set(arr)) == n:
            res += 1
        return N - res


s = Solution()
print(s.numDupDigitsAtMostN(111))
print(s.numDupDigitsAtMostN(102))
print(s.numDupDigitsAtMostN(20))
print(s.numDupDigitsAtMostN(255))
print(s.numDupDigitsAtMostN(100))
print(s.numDupDigitsAtMostN(99))
