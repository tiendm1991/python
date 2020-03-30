from datetime import datetime


class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        mod = 10 ** 9 + 7
        if n == 0:
            return 0

        def getKmp(pattern):
            n = len(pattern)
            if n == 0:
                return ''
            result = [0] * n
            i, j = 1, 0
            while i < n:
                if pattern[i] == pattern[j]:
                    result[i] = j + 1
                    i += 1
                    j += 1
                elif j == 0:
                    i += 1
                else:
                    j = result[j - 1]
            return result

        kmp = getKmp(evil)
        p = len(evil)
        dp = [[[[-1 for y in range(2)] for x in range(2)] for j in range(p+1)] for i in range(n+1)]

        def dfs(dp, idx, suffix,  eqS1, eqS2):
            if suffix == p:
                return 0
            if idx == n:
                return 1
            if dp[idx][suffix][int(eqS1)][int(eqS2)] != -1:
                return dp[idx][suffix][int(eqS1)][int(eqS2)]
            first = s1[idx] if eqS1 else 'a'
            last = s2[idx] if eqS2 else 'z'
            res = 0
            for i in range(ord(first), ord(last) + 1):
                ch = chr(i)
                j = suffix
                while j > 0 and evil[j] != ch:
                    j = kmp[j - 1]
                if evil[j] == ch:
                    j += 1
                res += dfs(dp, idx + 1, j, eqS1 and ch == s1[idx], eqS2 and ch == s2[idx])
            dp[idx][suffix][int(eqS1)][int(eqS2)] = res
            return res % mod

        return dfs(dp, 0, 0, True, True) % mod


pattern = Solution()
startTime = datetime.now()
print(pattern.findGoodStrings(3,"szc","zyi","p"))
print(datetime.now() - startTime)
