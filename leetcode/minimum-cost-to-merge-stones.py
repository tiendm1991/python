class Solution:
    def mergeStones(self, a, k: int) -> int:
        n = len(a)
        if (n - 1) % (k - 1) != 0:
            return -1
        pre = [0] * (n + 1)
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + a[i - 1]
        dp = {}

        def solve(i, j, m):
            res = float("inf")
            if (j - i + 1 - m) % (k - 1) != 0:
                return res
            if i == j:
                return 0 if m == 1 else res
            key = (i, j, m)
            if key in dp:
                return dp[key]
            if m == 1:
                return pre[j] - pre[i - 1] + solve(i, j, k)
            for mid in range(i, j, k - 1):
                res = min(res, solve(i, mid, 1) + solve(mid + 1, j, m - 1))
            dp[key] = res
            return res

        return solve(1, n, 1)


s = Solution()
print(s.mergeStones([3, 5, 1, 2, 6], 3))
print(s.mergeStones([3, 5, 1, 2, 6, 3, 4], 3))
print(s.mergeStones([2, 3, 5, 1, 2, 6, 3, 4, 7], 3))
print(s.mergeStones([3, 2, 4, 1], 2))
print(s.mergeStones([16, 43, 87, 30, 4, 98, 12, 30, 47, 45, 32, 4, 64, 14, 24, 84, 86, 51, 11, 22, 4], 2))
