class Solution:
    def waysToSplit_binarysearch(self, nums) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        res = 0
        pre = [0] * (n + 1)
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + nums[i - 1]

        def biSearch(l, r):
            s3 = pre[n] - pre[r]
            l1, r1 = l, r - 1
            while l1 < r1:
                m = (l1 + r1) // 2
                s2 = pre[r] - pre[m]
                if s2 <= s3:
                    r1 = m
                else:
                    l1 = m + 1
            l2, r2 = l, r - 1
            while l2 < r2:
                m = (l2 + r2 + 1) // 2
                s1, s2 = pre[m], pre[r] - pre[m]
                if s1 <= s2:
                    l2 = m
                else:
                    r2 = m - 1
            if l1 == l2:
                return 1 if pre[l1] <= pre[r] - pre[l1] <= s3 else 0
            return max(l2 - l1 + 1, 0)

        for i2 in range(n - 1, 1, -1):
            res = (res + biSearch(1, i2)) % mod
        return res

    def waysToSplit(self, nums) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        res = 0
        pre = [0] * (n + 1)
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + nums[i - 1]

        i1, i2 = n - 2, n - 2
        for i in range(n - 1, 1, -1):
            s3 = pre[n] - pre[i]
            while i1 >= 1 and pre[i] - pre[i1] <= s3:
                i1 -= 1
            while i2 > 1 and (pre[i2] > pre[i] - pre[i2] or i2 == i):
                i2 -= 1
            if i1 + 1 < i2:
                res = (res + (i2 - i1)) % mod
            elif i1 + 1 == i2 and pre[i2] <= pre[i] - pre[i2] <= s3:
                res = (res + 1) % mod
        return res


s = Solution()
print(s.waysToSplit([1, 2, 2, 2, 5, 0]))
print(s.waysToSplit([5, 9, 7, 5, 7, 9, 7]))
print(s.waysToSplit([0, 0, 0]))
print(s.waysToSplit([7, 0, 5]))
print(s.waysToSplit([0, 0, 0, 0]))
