class Solution:
    def numSubarrayProductLessThanK(self, nums, k: int) -> int:
        if k <= min(nums):
            return 0
        nums.append(k + 1)
        n = len(nums)
        start = 0
        while nums[start] >= k:
            start += 1
        m = nums[start]
        ans = 1
        for i in range(1, n):
            x = nums[i]
            m *= x
            while start <= i and m >= k:
                m /= nums[start]
                start += 1
            if start <= i:
                ans += i - start + 1
        return ans


s = Solution()
print(s.numSubarrayProductLessThanK([1, 2, 3], 0))
print(s.numSubarrayProductLessThanK([1, 1, 1], 1))
print(s.numSubarrayProductLessThanK([10, 5, 2, 6], 100))
