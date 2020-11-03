import string


class Solution:
    def numWays(self, words, target: str) -> int:
        mod = 10 ** 9 + 7
        n = len(words[0])
        m = len(target)
        countCharAt = {c: [0] * n for c in string.ascii_lowercase}
        for w in words:
            for i, c in enumerate(w):
                countCharAt[c][i] += 1
        dp = [[-1 for j in range(m)] for i in range(n)]

        def helper1(idxW, idxT):
            if idxT == m:
                return 1
            if idxW == n:
                return 0
            if dp[idxW][idxT] != -1:
                return dp[idxW][idxT]
            ans = 0
            if countCharAt[target[idxT]][idxW] != 0:
                ans = (countCharAt[target[idxT]][idxW] * help(idxW + 1, idxT + 1)) % mod
            ans = (ans + help(idxW + 1, idxT)) % mod
            dp[idxW][idxT] = ans
            return ans

        def helper(idxW, idxT):
            if idxT == m:
                return 1
            if idxW == n:
                return 0
            if dp[idxW][idxT] != -1:
                return dp[idxW][idxT]
            ans = helper(idxW + 1, idxT)
            if countCharAt[target[idxT]][idxW] != 0:
                ans = (ans + countCharAt[target[idxT]][idxW] * helper(idxW + 1, idxT + 1)) % mod
            dp[idxW][idxT] = ans
            return ans

        return helper(0, 0), helper1(0, 0)


s = Solution()
print(s.numWays(["acca", "bbbb", "caca"], "aba"))
