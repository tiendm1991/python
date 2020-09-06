# https://leetcode.com/problems/image-overlap/
class Solution:
    def largestOverlap(self, a, b) -> int:
        n = len(a)
        idxA, idxB = [], []
        d = {}
        for i in range(n):
            for j in range(n):
                # extend matrix by 4 way with length n - 1 => matrix bound = 3n-2
                # (n-1) * (3n-2) + i * (3n-2) + (n-1) + j
                # => (n-1) * (3n-1) + i * (3n-2) + j
                x = (n - 1) * (3 * n - 1) + (3 * n - 2) * i + j
                if a[i][j] == 1:
                    idxA.append(x)
                if b[i][j] == 1:
                    idxB.append(x)
        ans = 0
        for x in idxA:
            for y in idxB:
                move = y - x
                d[move] = d.get(move, 0) + 1
                ans = max(ans, d[move])
        return ans


s = Solution()
print(s.largestOverlap([[0, 1], [1, 1]],
                       [[1, 1], [1, 0]]))
print(s.largestOverlap([[1, 1, 0], [0, 1, 0], [0, 1, 0]],
                       [[0, 0, 0], [0, 1, 1], [0, 0, 1]]))
