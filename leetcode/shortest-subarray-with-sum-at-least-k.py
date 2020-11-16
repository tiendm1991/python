import collections


class Solution:
    def shortestSubarray(self, a, k: int) -> int:
        n = len(a)
        pre = [0] * (n + 1)
        res = n + 1
        q = collections.deque([])
        for i in range(n):
            pre[i + 1] = pre[i] + a[i]
        for i in range(n + 1):
            while q and pre[q[-1]] >= pre[i]:
                q.pop()
            left = -1
            while q and pre[i] - pre[q[0]] >= k:
                left = q.popleft()
            if left > -1:
                res = min(res, i - left)
            q.append(i)
        return res if res <= n else -1


s = Solution()
print(s.shortestSubarray([77, 19, 35, 10, -14], 19))
# print(s.shortestSubarray([2, -1, 2], 3))
