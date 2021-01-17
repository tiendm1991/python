class Solution:
    def minimumTimeRequired_slow(self, jobs, k: int) -> int:
        dp = {}
        n = len(jobs)

        def backtrack(a, i):
            if i == n:
                return max(a)
            key = (tuple(sorted(a)), i)
            if key in dp:
                return dp[key]
            res = float("inf")
            for j in range(k):
                a[j] += jobs[i]
                res = min(res, backtrack(a, i + 1))
                a[j] -= jobs[i]
            dp[key] = res
            return res

        return backtrack([0] * k, 0)

    def minimumTimeRequired(self, jobs, k: int) -> int:
        dp = {}
        n = len(jobs)
        resGlobal = [float("inf")]

        def backtrack(a, i):
            m = max(a)
            if i == n:
                return m
            if m >= resGlobal[0]:
                return resGlobal[0]
            key = (tuple(sorted(a)), i)
            if key in dp:
                return dp[key]
            res = float("inf")
            for j in range(k):
                a[j] += jobs[i]
                res = min(res, backtrack(a, i + 1))
                a[j] -= jobs[i]
            dp[key] = res
            resGlobal[0] = min(resGlobal[0], res)
            return res

        return backtrack([0] * k, 0)


s = Solution()
print(s.minimumTimeRequired([38, 49, 91, 59, 14, 76, 84], 3))
print(s.minimumTimeRequired([1, 2, 4, 7, 8], 2))
print(s.minimumTimeRequired([685, 314, 222, 532, 411, 882, 724, 851, 649, 161, 100, 540], 8))
