class Solution:
    def splitArraySameAverage1(self, a) -> bool:
        s, n = sum(a), len(a)
        if n == 1:
            return False
        dp = set()

        def backtrack(sCheck, nCheck, start):
            if nCheck > n // 2:
                return False
            if sCheck != 0 and sCheck * n == s * nCheck:
                return True
            if (sCheck, nCheck, start) in dp:
                return False
            dp.add((sCheck, nCheck, start))
            for i in range(start, n):
                if backtrack(sCheck + a[i], nCheck + 1, i + 1):
                    return True
            dp.add((sCheck, nCheck, start))
            return False

        return backtrack(0, 0, 0)

    def splitArraySameAverage(self, a) -> bool:
        s, n = sum(a), len(a)
        if n == 1:
            return False
        dp = {}

        def findSubset(subSum, k, idx):
            if k == 0:
                return subSum == 0
            if idx == n:
                return False
            if (subSum, k, idx) in dp:
                return dp[(subSum, k, idx)]
            dp[(subSum, k, idx)] = findSubset(subSum - a[idx], k - 1, idx + 1) or findSubset(subSum, k, idx + 1)
            return dp[(subSum, k, idx)]

        for j in range(1, n // 2 + 1):
            if s * j % n == 0 and findSubset(s * j // n, j, 0):
                return True
        return False


s = Solution()
print(s.splitArraySameAverage([3, 1, 2]), s.splitArraySameAverage1([3, 1, 2]))
print(s.splitArraySameAverage([3, 4, 22, 24, 26, 34, 35, 37, 44, 46, 52, 53, 55, 71, 73, 95, 96, 97]),
      s.splitArraySameAverage1([3, 4, 22, 24, 26, 34, 35, 37, 44, 46, 52, 53, 55, 71, 73, 95, 96, 97]))
print(s.splitArraySameAverage([73, 37, 34, 95, 4, 97, 22, 53, 55, 52, 46, 44, 71, 24, 26, 35, 96, 3]),
      s.splitArraySameAverage1([73, 37, 34, 95, 4, 97, 22, 53, 55, 52, 46, 44, 71, 24, 26, 35, 96, 3]))
print(s.splitArraySameAverage([1, 3]), s.splitArraySameAverage1([1, 3]))
print(s.splitArraySameAverage([1, 2, 3, 4, 5, 6, 7, 8]), s.splitArraySameAverage1([1, 2, 3, 4, 5, 6, 7, 8]))
