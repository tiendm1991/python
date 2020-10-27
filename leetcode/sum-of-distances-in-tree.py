class Solution:
    def sumOfDistancesInTree(self, n: int, edges):
        d = {i: [] for i in range(n)}
        for e in edges:
            d[e[0]].append(e[1])
            d[e[1]].append(e[0])
        sumDis = [0] * n
        countV = [0] * n

        def dfs1(u, p):
            countV[u] += 1
            for v in d[u]:
                if v == p:
                    continue
                dfs1(v, u)
                countV[u] += countV[v]
                sumDis[u] += sumDis[v] + countV[v]

        def dfs2(u, p):
            for v in d[u]:
                if v == p:
                    continue
                sumDis[v] = sumDis[u] + n - 2 * countV[v]
                dfs2(v, u)

        dfs1(0, -1)
        dfs2(0, -1)
        return sumDis


s = Solution()
print(s.sumOfDistancesInTree(6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))
