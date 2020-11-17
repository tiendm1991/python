class Solution:
    def minOperations(self, nums, x: int) -> int:
        n = len(nums)
        a, b = [0], [0]
        for i in nums:
            a.append(a[-1] + i)
            if a[-1] >= x:
                break
        for i in nums[::-1]:
            b.append(b[-1] + i)
            if b[-1] >= x:
                break
        ans = n + 1
        if a[-1] == x:
            ans = len(a)
        if b[-1] == x:
            ans = min(ans, len(b))
        if b:
            for i, v in enumerate(a):
                l, r = 0, len(b) - 1
                while l <= r:
                    m = (l + r) // 2
                    if b[m] == x - v:
                        ans = min(ans, m + i)
                        break
                    elif b[m] < x - v:
                        l = m + 1
                    else:
                        r = m - 1
        return ans if ans <= n else -1


s = Solution()
print(s.minOperations([1, 1, 4, 2, 3], 5))
print(s.minOperations([3, 2, 20, 1, 1, 3], 10))