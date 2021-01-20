import heapq


class Solution:
    def smallestDistancePair(self, nums, k: int) -> int:
        def count(v):
            ans = 0
            for i in range(1, n):
                left, right = 0, i
                while left < right:
                    mid = (left + right) // 2
                    if nums[i] - nums[mid] > v:
                        left = mid + 1
                    else:
                        right = mid
                ans += i - left
            return ans

        nums.sort()
        n = len(nums)
        M = nums[-1] - nums[0]
        l, r = 0, M
        while l < r:
            m = (l + r) // 2
            if count(m) < k:
                l = m + 1
            else:
                r = m
        return l


s = Solution()
print(s.smallestDistancePair([62, 100, 4], 2))
# print(s.smallestDistancePair([1, 3, 1], 1))
