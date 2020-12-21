import collections


class Solution:
    def removeStones(self, a) -> int:
        n = len(a)
        dx = {}
        dy = {}
        for i, p in enumerate(a):
            if p[0] not in dx:
                dx[p[0]] = {i}
            else:
                dx[p[0]].add(i)
            if p[1] not in dy:
                dy[p[1]] = {i}
            else:
                dy[p[1]].add(i)
        color = [-1] * n

        def dfs(i, c):
            color[i] = c
            p = a[i]
            for x in dx[p[0]]:
                if color[x] == -1:
                    dfs(x, c)
            for y in dy[p[1]]:
                if color[y] == -1:
                    dfs(y, c)

        col = 0
        for i in range(n):
            if color[i] == -1:
                dfs(i, col)
                col += 1
        d = collections.Counter(color)
        return sum([d[c] - 1 for c in d])


s = Solution()
print(s.removeStones([[0, 1], [1, 0]]))
# print(s.removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]))
# print(s.removeStones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]))
