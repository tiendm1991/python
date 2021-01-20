class Solution:
    def triangleNumber(self, nums) -> int:
        nums.sort()
        n = len(nums)
        if n < 3:
            return 0
        ans = 0
        for k in range(2, n):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    ans += j - i
                    j -= 1
                else:
                    i += 1
        return ans


s = Solution()
print(s.triangleNumber([2, 2, 3, 4]))
