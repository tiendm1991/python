class Solution:
    def shoppingOffers(self, price, special, needs) -> int:
        n = len(price)
        if n == 0:
            return 0
        dp = {}

        def help(need):
            ans = sum([price[j] * need[j] for j in range(n)])
            if ans == 0:
                return 0
            t = tuple(need)
            if t in dp:
                return dp[t]
            for sp in special:
                nextNeed = [need[j] - sp[j] for j in range(n)]
                if len([1 for j in range(n) if nextNeed[j] >= 0]) == n:
                    x = sp[-1] + help(nextNeed)
                    ans = min(ans, x)
            dp[t] = ans
            return ans

        return help(needs)


s = Solution()
print(s.shoppingOffers([1, 2, 3, 1, 9, 9]
                       , [[6, 3, 5, 6, 1, 0, 17], [6, 6, 6, 5, 2, 2, 2], [5, 2, 2, 1, 4, 1, 1], [6, 4, 4, 4, 0, 4, 19],
                          [4, 6, 0, 1, 0, 4, 3], [1, 2, 0, 5, 0, 4, 13], [2, 5, 1, 0, 0, 3, 8], [4, 3, 1, 3, 5, 3, 11],
                          [6, 1, 0, 1, 5, 6, 23], [5, 3, 1, 0, 3, 6, 7], [3, 4, 0, 6, 2, 1, 6], [0, 3, 6, 3, 4, 0, 2],
                          [2, 2, 3, 6, 3, 2, 1], [6, 1, 1, 4, 2, 0, 2], [5, 6, 6, 2, 1, 4, 20], [1, 4, 5, 2, 5, 4, 9],
                          [2, 3, 2, 2, 5, 4, 4], [6, 6, 0, 3, 0, 6, 23], [0, 6, 1, 5, 6, 5, 2], [0, 0, 6, 0, 4, 5, 17],
                          [0, 0, 5, 2, 3, 5, 7], [6, 0, 5, 3, 6, 3, 2], [4, 3, 5, 4, 0, 6, 15], [6, 2, 1, 5, 2, 1, 15]]
                       , [5, 6, 5, 5, 6, 1]))
