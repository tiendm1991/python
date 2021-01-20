import string


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        mod = 10 ** 9 + 7
        d = {c: [-1, -1] for c in string.ascii_uppercase}
        ans = 0
        for i, c in enumerate(s):
            k, j = d[c]
            ans = (ans + (j - k) * (i - j)) % mod
            d[c] = [j, i]
        for c in d:
            j, i = d[c]
            ans = (ans + (i - j) * (len(s) - i)) % mod
        return ans


s = Solution()
print(s.uniqueLetterString("ABA"))
