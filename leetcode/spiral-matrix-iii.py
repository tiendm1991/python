class Solution:
    def spiralMatrixIII(self, r: int, c: int, r0: int, c0: int):
        n = r * c
        res = [[0, 0] for i in range(n)]
        res[0] = [r0, c0]

        idx, k = 1, 1
        x, y = r0, c0
        while idx < n:
            for i in range(k):
                y += 1
                if 0 <= x < r and 0 <= y < c:
                    res[idx] = [x, y]
                    idx += 1
            for i in range(k):
                x += 1
                if 0 <= x < r and 0 <= y < c:
                    res[idx] = [x, y]
                    idx += 1
            k += 1
            for i in range(k):
                y -= 1
                if 0 <= x < r and 0 <= y < c:
                    res[idx] = [x, y]
                    idx += 1
            for i in range(k):
                x -= 1
                if 0 <= x < r and 0 <= y < c:
                    res[idx] = [x, y]
                    idx += 1
            k += 1
        return res


s = Solution()
print(s.spiralMatrixIII(5, 6, 1, 4))
