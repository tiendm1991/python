from datetime import datetime, time
import heapq


class Solution:
    def findDiagonalOrder(self, matrix):
        m = len(matrix)
        if m == 0:
            return []
        if m == 1:
            return matrix[0]
        n = len(matrix[0])

        def add(r, c):
            new = []
            while r < m and c >= 0:
                new.append(matrix[r][c])
                r += 1
                c -= 1
            return new

        a = []
        r = min(m, n)
        for i in range(r):
            a.append(add(0, i))
        if r == m:
            for i in range(r, n):
                a.append(add(0, i))
        for i in range(1, m):
            a.append(add(i, n - 1))
        reverse = True
        result = []
        for arr in a:
            if reverse:
                arr.reverse()
            result += arr
            reverse = not reverse
        return result


s = Solution()
startTime = datetime.now()
print(s.findDiagonalOrder([[1, 2, 3, 4, 5],
                           [6, 7, 8, 9, 10],
                           [11, 12, 13, 14, 15]]))
print(datetime.now() - startTime)
