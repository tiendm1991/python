class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        n = len(a)

        def valid(x):
            l, r = 0, len(x) - 1
            while l < r:
                if x[l] != x[r]:
                    return False
                l += 1
                r -= 1
            return True

        def help(x, y):
            i = 0
            while i < n and x[i] == y[i]:
                i += 1
            if i >= n // 2:
                return True
            return valid(x[i: n - i]) or valid(y[i: n - i])

        ra, rb = a[::-1], b[::-1]
        return help(a, rb) or help(b, ra)


s = Solution()
print(s.checkPalindromeFormation("askxrrnhyddrlmcgymtichivmwyjfpyqqxmiimxqqypfjywmvihcitmygcmlryczoygimgii",
                                 "iigmigyozcyfxgfzkwpvjuxbjphbbmwlhdcavhtjhbpccsxaaiyitfbzljvhjoytfqlqrohv"))
# print(s.checkPalindromeFormation("ulacfd", "jizalu"))
