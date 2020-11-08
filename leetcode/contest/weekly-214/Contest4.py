import bisect


class Solution:
    def createSortedArray(self, instructions) -> int:
        mod = 10 ** 9 + 7
        nums = []
        n = len(instructions)
        if n < 2:
            return 0

        def insert(x):
            left, right = bisect.bisect_left(nums, x), len(nums) - bisect.bisect_right(nums, x)
            bisect.insort(nums, x)
            return min(left, right)

        ans = 0
        for x in instructions:
            if not nums:
                nums = [x]
                continue
            ans = (ans + insert(x)) % mod
        return ans


s = Solution()
print(s.createSortedArray([1, 3, 3, 3, 2, 4, 2, 1, 2]))
print(s.createSortedArray([1, 2, 3, 6, 5, 4]))
print(s.createSortedArray([1, 5, 6, 2]))
