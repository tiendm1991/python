class Solution:
    def bestRotation(self, a) -> int:
        n = len(a)
        d = [0] * (n + 1)
        for i, v in enumerate(a):
            # [start, end] is interval that increase 1 point
            # from d[start] increase 1 point, from d[end+1] decrease 1 point
            if i >= v:
                d[0] += 1
                d[i - v + 1] -= 1
                d[i + 1] += 1
                d[n] -= 1
            else:
                d[i + 1] += 1
                d[i + n - v + 1] -= 1
        ans, _max = -1, 0
        cur = 0
        for i in range(n):
            cur += d[i]
            if cur > _max:
                _max = cur
                ans = i
        return ans


s = Solution()
print(s.bestRotation([2, 3, 1, 4, 0]))
