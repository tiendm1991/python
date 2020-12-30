class Solution:
    def maxWidthRamp(self, a) -> int:
        n = len(a)
        stack, stack2 = [], []
        res = 0
        for i, x in enumerate(a):
            if not stack or x < a[stack[-1]]:
                stack.append(i)
        for i in range(n - 1, -1, -1):
            while stack and a[i] >= a[stack[-1]]:
                res = max(res, i - stack.pop())
        return res


s = Solution()
print(s.maxWidthRamp([6, 2, 5, 4, 2, 1, 3]))
print(s.maxWidthRamp([6, 2, 5, 4, 2, 1, 3]))
