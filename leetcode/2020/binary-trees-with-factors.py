class Solution:
    def numFactoredBinaryTrees(self, a) -> int:
        mod = 10 ** 9 + 7
        a.sort()
        n = len(a)
        if n == 1:
            return 1
        dp = {x: 1 for x in a}
        for i in range(1, n):
            for j in range(i):
                if a[i] % a[j] == 0 and a[i] // a[j] in dp:
                    dp[a[i]] = (dp[a[i]] + (dp[a[j]] * dp[a[i] // a[j]]) % mod) % mod
        return sum(dp.values()) % mod


s = Solution()
print(s.numFactoredBinaryTrees([2, 4, 16]))
print(s.numFactoredBinaryTrees([2, 4]))
print(s.numFactoredBinaryTrees([2, 4, 5, 10]))
