class Solution:
    def longestMountain1(self, a) -> int:
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

    def longestMountain(self, a) -> int:
        n = len(a)
        if n < 3:
            return 0
        ans, increase, decrease = 0, 1, 0
        for i in range(1, n):
            if a[i] > a[i - 1]:
                if decrease == 0:
                    increase += 1
                else:
                    ans = max(ans, increase + decrease)
                    increase = 2
                    decrease = 0
            elif a[i] < a[i - 1]:
                if increase > 1:
                    decrease += 1
                else:
                    decrease = 0
            else:
                ans = max(ans, increase + decrease)
                increase = 1
                decrease = 0
        if decrease > 0:
            ans = max(ans, increase + decrease)
        return ans if ans >= 3 else 0


s = Solution()
print(s.longestMountain([0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]))
# print(s.longestMountain([2, 1, 4, 7, 3, 2, 5]))
