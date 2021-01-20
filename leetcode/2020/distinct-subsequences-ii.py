import string


class Solution:
    def distinctSubseqII_n2(self, s: str) -> int:
        mod = 10 ** 9 + 7
        n = len(s)
        lastIdx = {c: -1 for c in string.ascii_lowercase}
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            c = s[i - 1]
            for j in range(i - 1, max(lastIdx[c] - 1, -1), -1):
                dp[i] = (dp[i] + dp[j]) % mod
            lastIdx[c] = i
        return sum(dp[1:]) % mod

    def distinctSubseqII(self, s: str) -> int:
        mod = 10 ** 9 + 7
        n = len(s)
        lastIdx = {c: -1 for c in string.ascii_lowercase}
        dp = [1] + [0] * n
        pre = [1] + [0] * n
        for i in range(1, n + 1):
            c = s[i - 1]
            dp[i] = (pre[i - 1] - pre[max(lastIdx[c] - 1, -1)]) % mod
            pre[i] = (dp[i] + pre[i - 1]) % mod
            lastIdx[c] = i
        return sum(dp[1:]) % mod


s = Solution()
print(s.distinctSubseqII("aba"))
print(s.distinctSubseqII("abc"))
print(s.distinctSubseqII("abacad"))
