class Solution:
    def minimumBoxes(self, n: int) -> int:
        def count(h):
            return h * (h + 1) * (h + 2) // 6

        l, r = 1, n
        while l < r:
            m = (l + r) // 2
            if count(m) >= n:
                r = m
            else:
                l = m + 1
        res = l * (l + 1) // 2
        s = count(l)
        while s - l >= n:
            res -= 1
            s -= l
            l -= 1
        return res


s = Solution()
print(s.minimumBoxes(60))
print(s.minimumBoxes(64))
print(s.minimumBoxes(16))
print(s.minimumBoxes(3))
print(s.minimumBoxes(4))
print(s.minimumBoxes(10))
