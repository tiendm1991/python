class Solution:
    def maxProduct(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        negative, pre = 1, 1
        ans = -10 ** 9
        for x in nums:
            if x == 0:
                negative, pre = 1, 1
                ans = max(ans, 0)
            else:
                pre *= x
                if pre > 0:
                    ans = max(ans, pre)
                else:
                    if negative == 1:
                        negative = pre
                    else:
                        ans = max(ans, pre // negative)
        return ans


s = Solution()
print(s.maxProduct([-2, 0, -1]))
