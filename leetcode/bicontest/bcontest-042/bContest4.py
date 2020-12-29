class Solution:
    def minMoves(self, nums, k: int) -> int:
        n = len(nums)
        count = 0
        i, j = nums.index(1), 0
        res = n
        while i < n and j < n:
            count += nums[j]
            if count == k:
                res = min(res, j - i + 1 - k)
                i += 1
                while i < n and nums[i] == 0:
                    i += 1
                count -= 1
            j += 1
        return res


s = Solution()
print(s.minMoves([1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1], 7))
# print(s.minMoves([1, 0, 0, 0, 0, 0, 1, 1], 3))
# print(s.minMoves([1, 0, 0, 0, 1, 0, 1, 0, 0, 1], 3))
