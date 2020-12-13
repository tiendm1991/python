import collections
import itertools


class Solution:
    def minimumIncompatibility(self, nums, k: int) -> int:
        d = collections.Counter(nums)
        n = len(nums)
        if k == n:
            return 0
        m = n // k
        for x in d:
            if d[x] > k:
                return -1
        nums.sort()
        dp = {}

        def helper(a):
            res = 10 ** 15
            if not a:
                return 0
            if a in dp:
                return dp[a]
            for c in itertools.combinations(a, m):
                s = set(c)
                if len(s) < m:
                    continue
                newA = []
                ma, mi = max(s), min(s)
                for x in a:
                    if x not in s:
                        newA.append(x)
                    else:
                        s.remove(x)
                res = min(res, ma - mi + helper(tuple(newA)))
            dp[a] = res
            return res

        return helper(tuple(nums))


s = Solution()
print(s.minimumIncompatibility([13, 4, 7, 3, 3, 1, 12, 9, 11, 10, 13, 3, 12, 7], 7))
print(s.minimumIncompatibility([6, 3, 8, 1, 3, 1, 2, 2], 4))
