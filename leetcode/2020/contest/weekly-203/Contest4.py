#  https://leetcode.com/problems/stone-game-v/
class Solution:
    def stoneGameV(self, a) -> int:
        n = len(a)
        pre = [0] * (n + 1)
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + a[i - 1]

        dp = {}

        def help(first, last):
            key = f'{first}-{last}'
            if first == last:
                return 0
            if first == last - 1:
                return min(a[last - 1], a[first - 1])
            if key in dp:
                return dp[key]
            ans = 0
            for i in range(first, last):
                if pre[i] - pre[first - 1] < pre[last] - pre[i]:
                    ans = max(ans, pre[i] - pre[first - 1] + help(first, i))
                elif pre[i] - pre[first - 1] > pre[last] - pre[i]:
                    ans = max(ans, pre[last] - pre[i] + help(i + 1, last))
                else:
                    ans = max(ans, pre[i] - pre[first - 1] + help(first, i),
                              pre[last] - pre[i] + help(i + 1, last))
            dp[key] = ans
            return ans

        return help(1, n)


s = Solution()
print(s.stoneGameV([9, 8, 2, 4, 6, 3, 5, 1, 7]))
# 9 17 19 23 29 32 37 38 45
