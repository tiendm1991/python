import heapq
import collections


class Solution:
    def matrixRankTransform(self, a):
        m, n = len(a), len(a[0])
        ans = [[0 for j in range(n)] for i in range(m)]
        maxR, maxC = [0] * m, [0] * n
        d = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                d[a[i][j]].append([i, j])

        def find(x, par):
            if par[x] != x:
                par[x] = find(par[x], par)
            return par[x]

        for v in sorted(d):
            p = [i for i in range(m + n)]
            mask = {}
            for i, j in d[v]:
                rx, ry = find(i, p), find(j + m, p)
                mask[rx] = max(mask.get(rx, 0), mask.get(ry, 0), max(maxR[i], maxC[j]) + 1)
                mask[ry] = max(mask.get(rx, 0), mask.get(ry, 0), max(maxR[i], maxC[j]) + 1)
                if rx < ry:
                    p[ry] = rx
                elif ry < rx:
                    p[rx] = ry
            for i, j in d[v]:
                ri, rj = find(i, p), find(j + m, p)
                comp = min(ri, rj)
                ans[i][j] = mask[comp]
                maxR[i] = ans[i][j]
                maxC[j] = ans[i][j]
        return ans


s = Solution()
print(s.matrixRankTransform([[-42, 13, 40, 11, 30, 29, -16, -33, -6, -43, 0, 23, -50, 5],
                             [-32, -29, -6, 21, 8, 7, -50, 49, 28, 19, 34, -19, 48, 7],
                             [-6, 5, 48, -49, -46, 9, 44, -5, 10, 45, -28, -17, 10, 1],
                             [12, -21, -14, -39, 28, -9, 30, -31, 24, -9, 30, 37, -28, -49],
                             [-34, -31, 44, 7, 30, -11, -16, -21, 6, -3, 40, 31, -18, 1],
                             [44, -33, -18, 49, 0, 47, 2, 33, 16, -29, 46, -11, -28, -25],
                             [-6, 17, -40, -9, -2, 29, -16, -1, 34, 45, -32, -41, -10, -15],
                             [-4, -45, 6, -43, -16, 15, 30, 21, 32, -49, -46, 1, 16, 23],
                             [18, 25, 32, -41, 22, 33, 20, -17, -26, 13, 16, 43, -2, -11],
                             [16, -1, 38, 21, -28, -49, 46, -11, -48, 3, 38, -43, -48, 11],
                             [2, 9, -24, -49, -18, -31, 16, 31, 6, -3, -40, -33, 6, -47],
                             [-40, -37, 26, 21, -16, 3, 10, -19, 44, 11, 18, -3, 28, -17],
                             [14, -43, -32, 39, 2, 9, 44, -37, -38, -43, -8, 3, -26, 25],
                             [20, 15, 22, -35, -32, 35, 10, 29, 24, -29, -18, -19, -8, -9]]))
print(s.matrixRankTransform([[20, -21, -19],
                             [-19, 4, 19],
                             [22, -19, 24],
                             [-19, -19, 19]]))
print(s.matrixRankTransform([[20, -21, 14],
                             [-19, -19, 19],
                             [22, -47, 24],
                             [-19, 4, 19]]))
