import collections


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        n = len(nums)
        q = collections.deque()
        ans = []
        for i in range(n):
            while q and i - q[0] >= k:
                q.popleft()
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            if i >= k - 1:
                ans.append(nums[q[0]])
        return ans


s = Solution()
print(s.maxSlidingWindow([1, -1], 1))
print(s.maxSlidingWindow([1, 3, -3, -1, 5, 3, 6, 7], 3))
print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
