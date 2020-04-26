import collections


class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            return 1
        zeros = [0] * (n)
        ones = [0] * (n)
        for i in range(n):
            if i == 0:
                zeros[i] = 0 if s[i] == '1' else 1
                ones[n - 1 - i] = 0 if s[n-1-i] == '0' else 1
            else:
                zeros[i] = zeros[i - 1]
                ones[n - 1 - i] = ones[n - i]
                if s[i] == '0':
                    zeros[i] += 1
                if s[n - i - 1] == '1':
                    ones[n - i - 1] += 1
        _max = 0
        for i in range(n - 1):
            _max = max(_max, zeros[i] + ones[i + 1])
        return max(_max, zeros[n - 1])

s = Solution()
print(s.maxScore("00"))