class Solution:
    def shortestToChar(self, s: str, c: str):
        n = len(s)
        ans = [n] * n
        stack = []
        for i in range(n):
            if s[i] == c:
                ans[i] = 0
                while stack:
                    idx = stack.pop()
                    ans[idx] = i - idx
            else:
                stack.append(i)
        stack = []
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                ans[i] = 0
                while stack:
                    idx = stack.pop()
                    ans[idx] = min(ans[idx], idx - i)
            else:
                stack.append(i)
        return ans


s = Solution()
print(s.shortestToChar("loveleetcode", 'e'))
