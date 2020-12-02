class Solution:
    def sumSubarrayMins(self, arr) -> int:
        mod = 10 ** 9 + 7
        n = len(arr)
        res = 0
        stack = []
        dp = {}
        for i, x in enumerate(arr):
            res += x
            while stack and arr[stack[-1]] >= x:
                res += (i - stack.pop()) * x
            if stack:
                res += dp[stack[-1]]
            res %= mod
            dp[i] = res
            stack.append(i)
        return res


s = Solution()
print(s.sumSubarrayMins([3, 1, 2, 4]))
# print(s.sumSubarrayMins([1, 5, 3, 9, 7, 2, 5, 6]))
