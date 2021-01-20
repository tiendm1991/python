import collections


class Solution:
    def constrainedSubsetSum_Slow(self, nums, k: int) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = nums[::]
        for i in range(1, n):
            for j in range(max(i - k, 0), i):
                dp[i] = max(dp[i], dp[j] + nums[i])
        return max(dp)

    def constrainedSubsetSum(self, nums, k: int) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = nums[::]
        deque = collections.deque()
        if dp[0] >= 0:
            deque.append(0)
        for i in range(1, n):
            dp[i] = nums[i]
            if deque:
                dp[i] += dp[deque[0]]
            while deque and deque[-1] - deque[0] >= k - 1:
                deque.popleft()
            while deque and (dp[deque[-1]] < dp[i] or dp[deque[-1]] < 0):
                deque.pop()
            if dp[i] >= 0:
                deque.append(i)
        return max(dp)


s = Solution()
print(s.constrainedSubsetSum([10, 2, -10, 5, 20], 2))
print(s.constrainedSubsetSum([-1, -2, -3], 1))
print(s.constrainedSubsetSum([10, -2, -10, -5, 20], 2))
print(s.constrainedSubsetSum([7, -5, -4, -3, 9], 3))
