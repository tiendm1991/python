class Solution:
    def minAreaRect(self, points) -> int:
        dx, dy = {}, {}
        for p in points:
            if p[1] in dy:
                dy[p[1]].append(p[0])
            else:
                dy[p[1]] = [p[0]]
            if p[0] in dx:
                dx[p[0]].append(p[1])
            else:
                dx[p[0]] = [p[1]]
        res = float('inf')
        for y1 in dy:
            a, n = dy[y1], len(dy[y1])
            if n < 2:
                continue
            for i in range(n - 1):
                for j in range(i + 1, n):
                    x1, x2 = a[i], a[j]
                    sy1 = set(dx[x1])
                    for y2 in dx[x2]:
                        if y2 != y1 and y2 in sy1:
                            res = min(res, abs(x2 - x1) * abs(y2 - y1))
        return res


s = Solution()
print(s.minAreaRect([[3, 2], [3, 1], [4, 4], [1, 1], [4, 3], [0, 3], [0, 2], [4, 0]]))
# print(s.minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]))
# print(s.minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]))
