import collections
import string


class Solution:
    res = 0

    def numTilePossibilities(self, tiles: str) -> int:
        self.res = 0
        n = len(tiles)
        d = collections.Counter(tiles)
        f = [1] * (n + 1)
        for i in range(1, n + 1):
            f[i] = f[i - 1] * i

        def comb(K, N):
            return f[N] // (f[K] * f[N - K])

        def calculate(d2):
            count = []
            for k in d2:
                if d2[k] > 0:
                    count.append(d2[k])
            if not count:
                return 0
            N = sum(count)
            ans = 1
            for i in range(len(count) - 1):
                ans *= comb(count[i], N)
                N -= count[i]
            return ans

        chars = sorted(d)

        def backtrack(d2, idx):
            self.res += calculate(d2)
            for j in range(idx, len(chars)):
                k = chars[j]
                for i in range(1, d[k] + 1):
                    d2[k] = i
                    backtrack(d2, j + 1)
                    del d2[k]

        backtrack({}, 0)
        return self.res


s = Solution()
print(s.numTilePossibilities("AABC"))
print(s.numTilePossibilities("AAB"))
print(s.numTilePossibilities("AAABBC"))
