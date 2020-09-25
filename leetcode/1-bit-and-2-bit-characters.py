class Solution:
    def isOneBitCharacter(self, bits) -> bool:
        def valid(a):
            n = len(a)
            dp = [False] * n
            dp[0] = a[0] == 0
            for i in range(1, n):
                if a[i] == 0:
                    dp[i] = True
                else:
                    dp[i] = not dp[i - 1]
            return dp[n - 1]

        return valid(bits[:-1])


s = Solution()
print(s.isOneBitCharacter([1, 0, 0]))
print(s.isOneBitCharacter([1, 1, 1, 0]))
