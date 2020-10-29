import string


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        mod = 10 ** 9 + 7
        d = {c: [-1, -1] for c in string.ascii_uppercase}
        dp = {c: 0 for c in string.ascii_uppercase}
        for i, c in enumerate(s):
            # if d[c][0] == -1:
            #     d[c][0] = i
            dp[c] = (dp[c] + i - d[c][1]) % mod
            d[c][1] = i
        for c in d:
            if d[c][1] > -1:
                dp[c] = (dp[c] + len(s) - (d[c][1] + 1)) % mod
        ans = 0
        for c in dp:
            ans = (ans + dp[c]) % mod
        return ans


s = Solution()
print(s.uniqueLetterString("ABA"))
