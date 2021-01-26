import functools


class Solution:
    def allCellsDistOrder_sort(self, R: int, C: int, r0: int, c0: int):
        def cmp(p1, p2):
            d1 = abs(p1[0] - r0) + abs(p1[1] - c0)
            d2 = abs(p2[0] - r0) + abs(p2[1] - c0)
            return d1 - d2

        res = [[i, j] for j in range(C) for i in range(R)]
        return sorted(res, key=functools.cmp_to_key(cmp))

    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        direct = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        res = []
        q = [[r0, c0]]
        visited = {(r0, c0)}
        while q:
            res += q
            newQ = []
            for p in q:
                for d in direct:
                    if 0 <= p[0] + d[0] < R and 0 <= p[1] + d[1] < C and (p[0] + d[0], p[1] + d[1]) not in visited:
                        newQ.append([p[0] + d[0], p[1] + d[1]])
                        visited.add((p[0] + d[0], p[1] + d[1]))
            q = newQ
        return res


s = Solution()
print(s.allCellsDistOrder(2, 3, 1, 2))
