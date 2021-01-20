class Solution:
    def atMostNGivenDigitSet(self, digits, N: int) -> int:
        s = str(N)
        n = len(s)
        m = len(digits)
        res = sum([m ** x for x in range(1, n)])
        i = 0
        while i < n:
            j = 0
            while j < m and digits[j] < s[i]:
                j += 1
            res += j * (m ** (n - i - 1))
            if j == m or digits[j] > s[i]:
                break
            else:
                i += 1
                if i == n:
                    res += 1
        return res


s = Solution()
print(s.atMostNGivenDigitSet(["3", "4", "8"], 4))
print(s.atMostNGivenDigitSet(["3", "5"], 4))
print(s.atMostNGivenDigitSet(["1", "3", "5", "7"], 100))
print(s.atMostNGivenDigitSet(["1", "4", "9"], 1000000000))
