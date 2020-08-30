class Solution:
    def numOfWays(self, nums) -> int:
        n, mod = len(nums), 10 ** 9 + 7
        dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
        dp[1][0], dp[1][1] = 1, 1
        for i in range(2, n + 1):
            for j in range(i + 1):
                if j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

        def help(a):
            if len(a) <= 2:
                return 1
            l = [a[i] for i in range(1, len(a)) if a[i] < a[0]]
            r = [a[i] for i in range(1, len(a)) if a[i] > a[0]]
            ansL = help(l) % mod
            ansR = help(r) % mod
            return (ansL * ansR * dp[len(a) - 1][len(l)]) % mod

        return help(nums) - 1


s = Solution()
print(s.numOfWays([3, 4, 5, 1, 2]))
print(s.numOfWays([3, 1, 2, 5, 4, 6]))
print(s.numOfWays([9, 4, 2, 1, 3, 6, 5, 7, 8, 14, 11, 10, 12, 13, 16, 15, 17, 18]))
