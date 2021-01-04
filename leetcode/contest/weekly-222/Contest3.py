class Solution:
    def waysToSplit(self, nums) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        res = 0
        pre = [0] * (n + 1)
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + nums[i - 1]

        def biSearch(l, r):
            s3 = pre[n] - pre[r]
            l1, r1 = l, r
            while l1 < r1:
                m = (l1 + r1 + 1) // 2
                s1, s2 = pre[m], pre[r] - pre[m]
                if s1 <= s2 <= s3:
                    l1 = m
                else:
                    r1 = m - 1
            l2, r2 = l, r
            while l2 < r2:
                m = (l2 + r2) // 2
                s1, s2 = pre[m], pre[r] - pre[m]
                if s1 <= s2 <= s3:
                    r2 = m
                else:
                    l2 = m + 1
            return max(l1 - l2 + 1, 0)

        for i2 in range(n - 1, 1, -1):
            res = (res + biSearch(1, i2)) % mod
        return res

        return res


s = Solution()
print(s.waysToSplit([1, 2, 2, 2, 5, 0]))
