class Solution:
    def findMinArrowShots(self, points) -> int:
        p = sorted(points, key=lambda x: x[1])
        n = len(p)
        if n < 2:
            return n
        ans = 1
        end = p[0][1]
        for i in range(1, n):
            if p[i][0] <= end:
                continue
            else:
                ans += 1
                end = p[i][1]
        return ans


s = Solution()
print(s.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]))
print(s.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))
print(s.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
