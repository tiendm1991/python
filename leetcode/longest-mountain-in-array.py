class Solution:
    def longestMountain(self, a) -> int:
        n = len(a)
        pre = [1 for i in range(n)]
        if n < 3:
            return 0
        for i in range(1, n):
            if a[i] > a[i - 1]:
                pre[i] = pre[i - 1] + 1
        post = [1] * n
        ans = 0
        for i in range(n - 2, 0, -1):
            if a[i] > a[i + 1]:
                post[i] = post[i + 1] + 1
                if post[i] > 1 and pre[i] > 1:
                    ans = max(ans, pre[i] + post[i] - 1)
        return ans


s = Solution()
print(s.longestMountain([2, 1, 4, 7, 3, 2, 5]))
