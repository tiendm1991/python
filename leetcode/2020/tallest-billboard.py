class Solution:
    def tallestBillboard_topdown(self, a) -> int:
        n = len(a)
        dp = {}
        a.sort()

        def recursive(s1, s2, i):
            if i == n:
                if s1 == s2:
                    return s1
                return -1
            key = (abs(s1 - s2), i)
            if key in dp:
                return -1 if dp[key] == -1 else dp[key] + min(s1, s2)
            a2 = recursive(s1 + a[i], s2, i + 1)
            a3 = recursive(s1, s2 + a[i], i + 1)
            a1 = recursive(s1, s2, i + 1)
            ans = max(a1, a2, a3)
            dp[key] = -1 if ans == -1 else ans - min(s1, s2)
            return ans

        return recursive(0, 0, 0)

    def tallestBillboard(self, a) -> int:
        dp = {0: 0}
        for x in a:
            newDp = {k: v for k, v in dp.items()}
            for diff, cur in newDp.items():
                # store min
                dp[diff + x] = max(newDp.get(diff + x, 0), cur)
                dp[abs(diff - x)] = max(dp.get(abs(diff - x), 0), min(cur + x, cur + diff))

                # store max
                # dp[diff + x] = max(dp.get(diff + x, 0), cur + x)
                # dp[abs(diff - x)] = max(dp.get(abs(diff - x), 0), max(cur, cur - diff + x))

        return dp[0]


s = Solution()
print(s.tallestBillboard([1, 2, 3, 4, 5, 6]))
print(s.tallestBillboard([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 50, 50, 50, 150, 150, 150, 100, 100, 100, 123]))
print(s.tallestBillboard([1, 2, 3, 6]))
