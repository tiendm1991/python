import math


class Solution:
    def waysToFillArray(self, queries):
        MAX = 10 ** 4
        MAX_PRIME = int(math.sqrt(MAX)) + 1
        mod = 10 ** 9 + 7
        # allPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
        #              43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        allPrimes = []
        p = [True] * (MAX_PRIME + 1)
        for i in range(2, MAX_PRIME + 1):
            if not p[i]:
                continue
            allPrimes.append(i)
            for j in range(i * i, MAX_PRIME + 1, i):
                p[j] = False

        def primeFactor(x):
            primeDict = {}
            i = 0
            while x > 1 and i < len(allPrimes):
                if x % allPrimes[i] == 0:
                    primeDict[allPrimes[i]] = primeDict.get(allPrimes[i], 0) + 1
                    x //= allPrimes[i]
                else:
                    i += 1
            if x > 1:
                primeDict[x] = primeDict.get(x, 0) + 1
            return primeDict

        def comb(n, k):
            r = 1
            if k == n:
                return 1
            if k == 1:
                return n
            for i in range(1, min(k, n - k) + 1):
                r = r * (n - i + 1) // i
            return r % mod

        def solve(n, k):
            d = primeFactor(k)
            r = 1
            for prime in d:
                m = d[prime]
                r = r * comb(n + m - 1, m) % mod
            return r

        res = []
        for q in queries:
            if q[0] == 1 or q[1] == 1:
                res.append(1)
            else:
                res.append(solve(q[0], q[1]))
        return res


s = Solution()
print(s.waysToFillArray([[306, 256]]))
print(s.waysToFillArray([[5, 12]]))
print(s.waysToFillArray([[5, 997]]))
