class Solution:
    def gardenNoAdj(self, n: int, paths):
        g = {i: set() for i in range(n)}
        for p in paths:
            g[p[0] - 1].add(p[1] - 1)
            g[p[1] - 1].add(p[0] - 1)
        maxColor = 4
        res = [0] * n
        for i in range(n):
            colors = {res[j] for j in g[i]}
            for j in range(1, maxColor + 1):
                if j not in colors:
                    res[i] = j
                    break
        return res


s = Solution()
print(s.gardenNoAdj(4, [[1, 2], [3, 4]]))
print(s.gardenNoAdj(4, [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]))
