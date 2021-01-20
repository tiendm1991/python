class Solution:
    def maximalNetworkRank(self, n: int, roads) -> int:
        d = {i: [] for i in range(n)}
        edges = set()
        for r in roads:
            d[r[0]].append(r[1])
            d[r[1]].append(r[0])
            edges.add(f"{r[0]}-{r[1]}")
            edges.add(f"{r[1]}-{r[0]}")
        ans = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                m = len(d[i]) + len(d[j])
                if f"{i}-{j}" in edges:
                    m -= 1
                ans = max(ans, m)
        return ans


s = Solution()
print(s.maximalNetworkRank(2, [[0, 1]]))
print(s.maximalNetworkRank(4, [[0, 1], [0, 3], [1, 2], [1, 3]]))
