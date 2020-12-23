class Solution:
    def cherryPickup(self, a) -> int:
        m, n = len(a), len(a[0])
        dp = {}

        def helper(r, c1, c2):
            if r == m or c1 < 0 or c1 == n or c2 < 0 or c2 == n:
                return 0
            if (r, c1, c2) in dp:
                return dp[(r, c1, c2)]
            res = a[r][c1] if c1 == c2 else a[r][c1] + a[r][c2]
            maxCherry = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    maxCherry = max(maxCherry, helper(r + 1, c1 + i, c2 + j))
            res += maxCherry
            dp[(r, c1, c2)] = res
            return res

        return helper(0, 0, n - 1)


s = Solution()
print(s.cherryPickup([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]))
print(s.cherryPickup([[1, 0, 0, 0, 0, 0, 1], [2, 0, 0, 0, 0, 3, 0], [2, 0, 9, 0, 0, 0, 0], [0, 3, 0, 5, 4, 0, 0],
                      [1, 0, 2, 3, 0, 0, 6]]))
