# https://leetcode.com/problems/find-latest-group-of-size-m
class Solution:
    def findLatestStep(self, a, m: int) -> int:
        n = len(a)
        left, right = [0] * (n + 2), [0] * (n + 2)
        count = [0] * (n + 2)
        arr = [0] * (n + 2)
        ans = -1
        for i, x in enumerate(a):
            arr[x] = 1
            left[x], right[x] = x, x
            count[1] += 1
            if left[x - 1] != 0:
                left[x] = left[x - 1]
                right[left[x - 1]] = x
                count[1] -= 1
                count[x - left[x - 1]] -= 1  # x - 1 - left[x-1] + 1
                count[x - left[x - 1] + 1] += 1
            if right[x + 1] != 0:
                right[x] = right[x + 1]
                right[left[x]] = right[x + 1]
                left[right[x + 1]] = left[x]
                count[right[x + 1] - x] -= 1
                count[x - left[x] + 1] -= 1
                count[right[x] - left[x] + 1] += 1
            if count[m] > 0:
                ans = i + 1
        return ans


s = Solution()
print(s.findLatestStep([3, 1, 5, 4, 2], 2))
