class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ''
        result = [0] * n
        i, j = 1, 0
        while i < n:
            if s[i] == s[j]:
                result[i] = j + 1
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = result[j - 1]
        return s[:result[-1]]


s = Solution()
print(s.longestPrefix('bba'))
