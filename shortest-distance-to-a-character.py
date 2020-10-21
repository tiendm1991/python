class Solution:
    def shortestToChar(self, s: str, c: str):
        n = len(s)
        ans = [n] * n
        start = -1
        for i in range(n):
            if s[i] == c:
                start = i
                ans[i] = 0
            elif start != -1:
                ans[i] = i - start
        start = -1
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                start = i
            elif start != -1:
                ans[i] = min(ans[i], start - i)

        return ans


s = Solution()
print(s.shortestToChar("loveleetcode", 'e'))
