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
        q = [(-m, 0)]
        seen = {}
        # seen[i] means that we can arrive at node i and have seen[i] moves left
        while q:
            x, i = heapq.heappop(q)
            if i in seen:
                continue
            seen[i] = -x
            if i not in d:
                continue
            for j in d[i]:
                x2 = -x - d[i][j] - 1
                if j not in seen and x2 >= 0:
                    heapq.heappush(q, (-x2, j))
        res = len(seen)
        for i, j, k in edges:
            res += min(seen.get(i, 0) + seen.get(j, 0), k)
        return seen, res


s = Solution()
print(s.reachableNodes([[0, 1, 10], [0, 2, 1], [1, 2, 2]], 6, 3))
print(s.reachableNodes([[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]], 10, 4))
