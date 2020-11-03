class Solution:
    def maxWidthOfVerticalArea(self, points) -> int:
        ans = 0
        a = sorted(x[0] for x in points)
        a.append(a[-1])
        for i in range(1, len(a)):
            ans = max(ans, a[i] - a[i - 1])
        return ans


s = Solution()
print(s.maxWidthOfVerticalArea([[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]))
