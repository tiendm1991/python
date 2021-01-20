import functools


class Solution:
    def largestNumber(self, nums) -> str:
        def compare(x, y):
            return int(str(y) + str(x)) - int(str(x) + str(y))

        nums = sorted(nums, key=functools.cmp_to_key(compare))
        ans = ""
        for x in nums:
            ans += str(x)
        return str(int(ans))


s = Solution()
print(s.largestNumber([3, 30, 34, 5, 9]))
