import collections


class Solution:
    def maxResult(self, a, k: int) -> int:
        n = len(a)
        dp = [0] * (n + 1)
        q = collections.deque()
        for i in range(1, n + 1):
            if not q:
                dp[i] = a[i - 1]
            else:
                dp[i] = a[i - 1] + dp[q[0]]
            while q and dp[q[-1]] <= dp[i]:
                q.pop()
            while q and i - q[0] >= k:
                q.popleft()
            q.append(i)
        return dp[n]


s = Solution()
print(s.maxResult([1, -1, -2, 4, -7, 3], 2))
print(s.maxResult([10, -5, -2, 4, 0, 3], 3))
print(s.maxResult([1, -5, -20, 4, -1, 3, -6, -3], 2))
