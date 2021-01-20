class Solution:
    def minMoves_slow(self, nums, k: int) -> int:
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

    def minMoves(self, nums, k: int) -> int:
        a = []
        for i, x in enumerate(nums):
            if x == 1:
                a.append(i)
        n = len(a)
        pre = [0] * (n + 1)
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + a[i - 1]
        res = float("inf")
        for i in range(n - k + 1):
            j = i + k - 1
            m = (i + j) // 2
            # a[i] .... a[m] .... a[j]
            # move_left = (a[m] - 1 + a[m] - 2 + ... + a[m] - (m - i)) - (a[i] + ... + a[m-1])
            # move_right = (a[m+1] + ... + a[j]) - (a[m] + 1 + a[m] + 2 + ... + a[m] + (j-m))
            move_left = ((a[m] - 1 + a[m] - (m - i)) * (m - i) // 2) - (pre[m] - pre[i])
            move_right = (pre[j + 1] - pre[m + 1]) - ((a[m] + 1 + a[m] + (j - m)) * (j - m) // 2)
            res = min(res, move_left + move_right)
        return res


s = Solution()
print(s.minMoves_slow([0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1], 6),
      s.minMoves([0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1], 6))
print(s.minMoves_slow([1, 0, 0, 1, 0, 1], 2),
      s.minMoves([1, 0, 0, 1, 0, 1], 2))
print(s.minMoves_slow([1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1], 7),
      s.minMoves([1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1], 7))
print(s.minMoves_slow([1, 0, 0, 0, 0, 0, 1, 1], 3),
      s.minMoves([1, 0, 0, 0, 0, 0, 1, 1], 3))
print(s.minMoves_slow([1, 0, 0, 0, 1, 0, 1, 0, 0, 1], 3),
      s.minMoves([1, 0, 0, 0, 1, 0, 1, 0, 0, 1], 3))
