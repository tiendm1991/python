class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        p = [i for i in range(n + 1)]

        def find(v):
            if v != p[v]:
                p[v] = find(p[v])
            return p[v]

        for x, y in edges:
            rx = find(x)
            ry = find(y)
            if rx == ry:
                return [x, y]
            p[ry] = rx
        return None
