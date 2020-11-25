import heapq


class Solution:
    def reachableNodes(self, edges, m: int, n: int) -> int:
        d = {}
        for i, j, k in edges:
            if i not in d:
                d[i] = {}
            if j not in d:
                d[j] = {}
            d[i][j] = k
            d[j][i] = k
        q = [(0, 0)]
        dis = [0] * n
        visited = set()
        while m >= 0 and q:
            x, i = heapq.heappop(q)
            if i in visited:
                continue
            for j in d[i]:
                if j not in visited and x - d[i][j] < dis[j]:
                    dis[j] = x - d[i][j]
                    heapq.heappush(q, (dis[j], j))
            visited.add(i)
            m -= 1
        if m < 0:
            return max(dis)
        res = 0
        for i in range(n):
            if 0 in d[i]:
                res = max(res, -dis[i] + d[i][0])
        return res


s = Solution()
print(s.reachableNodes([[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]], 10, 4))
print(s.reachableNodes([[0, 1, 10], [0, 2, 1], [1, 2, 2]], 6, 3))
