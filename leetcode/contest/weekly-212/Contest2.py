class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        def check(a):
            if len(a) == 2:
                return True
            x = a[1] - a[0]
            for i in range(2, len(a)):
                if a[i] - a[i - 1] != x:
                    return False
            return True

        m = len(l)
        ans = [False] * m
        for i in range(m):
            ans[i] = check(sorted(nums[l[i]: r[i] + 1]))
        return ans
