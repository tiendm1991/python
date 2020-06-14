from heapq import heappush
from heapq import heappop

class Node:
    def __init__(self, id, w, k):
        self.id = id
        self.w = w
        self.k = k

    def __lt__(self, other):
        return self.w < other.w

    def __str__(self):
        return f'{self.id}-{self.w}-{self.k}'


class Solution:
    def findCheapestPrice1(self, n: int, flights, src: int, dst: int, K: int) -> int:
        max_int = 10**9;
        edges = [[max_int for j in range(n)] for i in range(n)]
        for f in flights:
            edges[f[0]][f[1]] = f[2]
        memo = [[max_int for k in range(K+2)] for i in range(n)]
        def dfs(dest, k):
            if dest == src:
                return 0
            if k == 0:
                return max_int
            if memo[dest][k] < max_int:
                return memo[dest][k]
            res = max_int
            for v in range(n):
                if edges[v][dest] < max_int:
                    res = min(res, edges[v][dest] + dfs(v, k-1))
            memo[dest][k] = res
            return res
        result = dfs(dst, K+1)
        return result if result < max_int else -1

    def findCheapestPrice(self, n: int, flights, src: int, dst: int, K: int) -> int:
        max_int = 10**9;
        edges = {i: {} for i in range(n)}
        for f in flights:
            edges[f[0]][f[1]] = f[2]
        q = [Node(src, 0, 0)]
        while q:
            node = heappop(q)
            if node.k < K + 2:
                if node.id == dst:
                    return node.w
                for i in edges[node.id]:
                    heappush(q, Node(i, node.w + edges[node.id][i], node.k + 1))
        return -1


s = Solution()
print(s.findCheapestPrice(10, [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]],6,0,7))
print(s.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))