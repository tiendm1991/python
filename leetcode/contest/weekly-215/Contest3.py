class Solution:
    def minOperations_bisearch(self, nums, x: int) -> int:
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

    def minOperations_map(self, nums, x: int) -> int:
        n = len(nums)
        if n == 1:
            return 1 if nums[0] == x else -1
        pre, suf = [0] * (n + 1), [0] * (n + 1)
        res = n + 1
        d = {0: 0}
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + nums[i - 1]
            suf[i] = suf[i - 1] + nums[n - i]
            d[suf[i]] = i
        for i in range(n + 1):
            sufFind = x - pre[i]
            if sufFind in d and i < n - d[sufFind] + 1:
                res = min(res, i + d[sufFind])
        return res if res <= n else -1

    def minOperations(self, nums, x: int) -> int:
        n = len(nums)
        if n == 1:
            return 1 if nums[0] == x else -1
        pre, suf = [0] * (n + 1), [0] * (n + 1)
        res = n + 1
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + nums[i - 1]
            suf[i] = suf[i - 1] + nums[n - i]
        if pre[n] < x:
            return -1
        j = 0
        for i in range(n, -1, -1):
            if pre[i] + suf[j] > x:
                continue
            while pre[i] + suf[j] < x and i + j <= n:
                j += 1
            if pre[i] + suf[j] == x and i + j <= n:
                res = min(res, i + j)
        return res if res <= n else -1


s = Solution()
print(s.minOperations([1, 1, 4, 2, 3], 5))
print(s.minOperations([3, 2, 20, 1, 1, 3], 10))
