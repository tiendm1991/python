class Solution:
    def bagOfTokensScore(self, tokens, P: int) -> int:
        n = len(tokens)
        if n == 0:
            return 0
        tokens.sort()
        i, j = 0, n - 1
        ans = 0
        while i <= j:
            while i <= j and P >= tokens[i]:
                ans += 1
                P -= tokens[i]
                i += 1
            if j > i and ans > 0:
                P += tokens[j]
                j -= 1
                ans -= 1
            else:
                break
        return ans


s = Solution()
print(s.bagOfTokensScore([2], 5))
# print(s.bagOfTokensScore([71, 55, 82], 54))
print(s.bagOfTokensScore([100], 5))
print(s.bagOfTokensScore([1, 2, 3, 4], 2))
