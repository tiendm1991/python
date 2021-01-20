class Solution:
    def minDominoRotations(self, a, b) -> int:
        n = len(a)
        candidate = []
        for x in range(1, 7):
            count = 0
            for i in range(n):
                if a[i] == x or b[i] == x:
                    count += 1
            if count == n:
                candidate.append(x)
        if len(candidate) == 0:
            return -1
        ans = n
        for c in candidate:
            a1 = a.count(c)
            b1 = b.count(c)
            ans = min(ans, n - max(a1, b1))
        return ans


s = Solution()
print(s.minDominoRotations([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]))
