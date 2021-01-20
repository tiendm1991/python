class Solution:
    def catMouseGame(self, graph) -> int:
        n = len(graph)
        dp = [[[-1 for j in range(n)] for i in range(n)] for k in range(2 * n)]

        def search(t, pMouse, pCat):
            if pMouse == 0:
                return 1
            if pCat == pMouse:
                return 2
            if t == 2 * n:
                return 0
            if dp[t][pMouse][pCat] != -1:
                return dp[t][pMouse][pCat]
            res = -1
            isMouseTurn = t % 2 == 0
            if isMouseTurn:
                res = 2
                for pNext in graph[pMouse]:
                    resNext = search(t + 1, pNext, pCat)
                    if resNext == 1:
                        res = 1
                        break
                    elif resNext == 0:
                        res = 0
            else:
                res = 1
                for pNext in graph[pCat]:
                    if pNext == 0:
                        continue
                    resNext = search(t + 1, pMouse, pNext)
                    if resNext == 2:
                        res = 2
                        break
                    elif resNext == 0:
                        res = 0
            dp[t][pMouse][pCat] = res
            return res

        return search(0, 1, 2)


s = Solution()
print(s.catMouseGame([[3, 4], [3, 5], [3, 6], [0, 1, 2], [0, 5, 6], [1, 4], [2, 4]]))
print(s.catMouseGame([[2, 3], [3, 4], [0, 4], [0, 1], [1, 2]]))
print(s.catMouseGame([[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]))
print(s.catMouseGame([[1, 3], [0], [3], [0, 2]]))
