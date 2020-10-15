class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        mod = 10 ** 9 + 7
        n = len(s)
        if n < 2:
            return n
        dp = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[i] != s[j]:
                    dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1] + mod) % mod
                    continue
                left, right = i + 1, j - 1
                while left < j and s[left] != s[i]:
                    left += 1
                while right > i and s[right] != s[i]:
                    right -= 1
                dp[i][j] = 2 * dp[i + 1][j - 1]
                if left > right:
                    dp[i][j] += 2
                elif left == right:
                    dp[i][j] += 1
                else:
                    dp[i][j] -= dp[left + 1][right - 1]
                dp[i][j] %= mod
        return dp[0][n - 1]


s = Solution()
print(s.countPalindromicSubsequences("bcadcb"))
print(s.countPalindromicSubsequences("bcabca"))
print(s.countPalindromicSubsequences("dbcbaaacdcbabcbddaac"))
