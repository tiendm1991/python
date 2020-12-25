class Solution:
    def minDeletionSize(self, a) -> int:
        m, n = len(a), len(a[0])
        dp = [1 for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                check = True
                for k in range(m):
                    if a[k][i] < a[k][j]:
                        check = False
                        break
                if check:
                    dp[i] = max(dp[i], dp[j] + 1)
        return n - max(dp)


s = Solution()
print(s.minDeletionSize(["babca",
                         "bbazb"]))
