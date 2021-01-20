class Solution:
    def maxHeight(self, a) -> int:
        for c in a:
            c.sort()
        a.sort()
        n = len(a)
        dp = [a[i][2] for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                if all(a[i][k] >= a[j][k] for k in range(3)):
                    dp[i] = max(dp[i], dp[j] + a[i][2])
        return max(dp)


s = Solution()
print(s.maxHeight([[50, 45, 20], [95, 37, 53], [45, 23, 12]]))
print(s.maxHeight([[38, 25, 45], [76, 35, 3]]))
print(s.maxHeight([[7, 11, 17], [7, 17, 11], [11, 7, 17], [11, 17, 7], [17, 7, 11], [17, 11, 7]]))
