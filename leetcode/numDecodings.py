class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [0 for i in range(n)]
        dp[-1] = 1 if int(s[-1]) >= 1 and int(s[-1]) <= 26 else 0
        for i in range(n-2, -1, -1):
            if s[i] == '0':
                dp[i] = 0
                continue
            dp[i] = dp[i+1]
            if int(s[i] + s[i+1]) <= 26:
                if i < n-2:
                    dp[i] += dp[i+2]
                else:
                    dp[i] += 1

        def numDecodings2(self, s: str) -> int:
            n = len(s)
            if n == 0:
                return 0
            dp = [0 for i in range(n + 1)]
            dp[-1] = 1
            for i in range(n - 1, -1, -1):
                if s[i] == '0':
                    dp[i] = 0
                    continue
                dp[i] = dp[i + 1]
                if i < n - 1 and int(s[i] + s[i + 1]) <= 26:
                    dp[i] += dp[i + 2]
            return dp[0]
        return dp[0]