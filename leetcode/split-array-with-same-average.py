class Solution:
    def splitArraySameAverage(self, a) -> bool:
        s, n = sum(a), len(a)
        if n == 1:
            return False
        dp = set()
        a.sort()

        def backtrack(sCheck, nCheck, start):
            if  start == n:
                return
            if sCheck != 0 and sCheck * n == s * nCheck:
                return True
            if (sCheck, nCheck, start) in dp:
                return False
            dp.add((sCheck, nCheck, start))
            for i in range(start, n):
                if (sCheck + a[i]) * n > s * (nCheck + 1):
                    break
                if backtrack(sCheck + a[i], nCheck + 1, i + 1):
                    return True
            dp.add((sCheck, nCheck, start))
            return False

        return backtrack(0, 0, 0)


s = Solution()
print(s.splitArraySameAverage([73, 37, 34, 95, 4, 97, 22, 53, 55, 52, 46, 44, 71, 24, 26, 35, 96, 3]))
# print(s.splitArraySameAverage([1, 3]))
# print(s.splitArraySameAverage([1, 2, 3, 4, 5, 6, 7, 8]))
