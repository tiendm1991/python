class Solution:
    def catMouseGame(self, graph) -> int:
        n = len(graph)
        dp = [[[-1 for j in range(n)] for i in range(n)] for k in range(2 * n)]

        def search(t, pMouse, pCat):
            if pMouse == 0:
                return 1
            if pMouse == pCat:
                return 2
            if t == 2 * n:
                return 0
            if dp[t][pMouse][pCat] != -1:
                return dp[t][pMouse][pCat]


            res = -1
            dp[t][pMouse][pCat] = res
            return res

        return search(0, 1, 2)


s = Solution()
print(s.catMouseGame([[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]))
