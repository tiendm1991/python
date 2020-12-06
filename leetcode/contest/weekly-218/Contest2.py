class Solution:
    def maxOperations(self, nums, k: int) -> int:
        d = {}
        res = 0
        for i, x in enumerate(nums):
            if k - x in d and d[k - x] > 0:
                d[k - x] -= 1
                res += 1
            else:
                d[x] = d.get(x, 0) + 1
        return res


s = Solution()
print(s.maxOperations([1, 2, 3, 4], 5))
print(s.maxOperations([3, 1, 3, 4, 3], 6))
