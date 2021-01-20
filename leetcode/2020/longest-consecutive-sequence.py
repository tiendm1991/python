# https://leetcode.com/problems/longest-consecutive-sequence/
class Solution:
    def longestConsecutive(self, a) -> int:
        left, right, visited = {}, {}, {}
        ans = 0
        for i, x in enumerate(a):
            if x in visited:
                continue
            left[x], right[x] = x, x
            if x - 1 in left:
                left[x] = left[x - 1]
                right[left[x - 1]] = x
            if x + 1 in right:
                right[x] = right[x + 1]
                right[left[x]] = right[x + 1]
                left[right[x + 1]] = left[x]
            ans = max(ans, right[x] - left[x] + 1)
            visited[x] = True
        return ans


s = Solution()
print(s.longestConsecutive([-1, 9, -3, -6, 7, 6, 8, 6, 5, 2]))
