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
    def constrainedSubsetSum_Clear(self, nums, k: int) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = nums[::]
        deque = collections.deque()
        if dp[0] >= 0:
            deque.append(dp[0])
        for i in range(1, n):
            dp[i] = nums[i]
            if deque:
                dp[i] += deque[0]
            if len(deque) == k:
                deque.popleft()
            while deque and (deque[-1] < dp[i] or deque[-1] < 0):
                deque.pop()
            if dp[i] >= 0:
                deque.append(dp[i])
        return max(dp)

    def constrainedSubsetSum_Short(self, nums, k: int) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = nums[::]
        deque = collections.deque()
        deque.append(max(dp[0], 0))
        for i in range(1, n):
            dp[i] = nums[i] + deque[0]
            if len(deque) == k:
                deque.popleft()
            while deque and deque[-1] <= dp[i]:
                deque.pop()
            deque.append(max(dp[i], 0))
        return max(dp)
s = Solution()
print(s.constrainedSubsetSum([10,-2,-10,-5,20], 2))