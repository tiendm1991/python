class Solution:
    def longestOnes(self, a, k: int) -> int:
        i = 0
        res = 0
        zeros = 0
        for j, x in enumerate(a):
            zeros += 1 if x == 0 else 0
            while i <= j and zeros > k:
                if a[i] == 0:
                    zeros -= 1
                i += 1
            res = max(res, j - i + 1)
        return res


s = Solution()
# print(s.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
# print(s.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
print(s.longestOnes([0, 0,  0, 0], 0))
