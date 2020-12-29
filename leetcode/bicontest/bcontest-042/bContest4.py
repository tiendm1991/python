class Solution:
    def minMoves(self, nums, k: int) -> int:
        a = []
        for i, x in enumerate(nums):
            if x == 1:
                a.append(i)
        n = len(a)
        res = float("inf")
        for i in range(n - k + 1):
            j = i + k - 1
            m = (i + j) // 2
            sub_res = 0
            for delta in range(1, m - i + 1):
                sub_res += (a[m] - delta) - a[m - delta]
            for delta in range(1, j - m + 1):
                sub_res += a[m + delta] - (a[m] + delta)
            res = min(res, sub_res)
        return res


s = Solution()
print(s.minMoves([0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1], 6))
# print(s.minMoves([1, 0, 0, 1, 0, 1], 2))
# print(s.minMoves([1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1], 7))
# print(s.minMoves([1, 0, 0, 0, 0, 0, 1, 1], 3))
# print(s.minMoves([1, 0, 0, 0, 1, 0, 1, 0, 0, 1], 3))
