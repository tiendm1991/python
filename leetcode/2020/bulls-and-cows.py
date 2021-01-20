import collections


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret)
        e = [1 for i in range(n) if secret[i] == guess[i]]
        a = [secret[i] for i in range(n) if secret[i] != guess[i]]
        b = [guess[i] for i in range(n) if secret[i] != guess[i]]
        na, nb = len(e), 0
        s = collections.Counter(a)
        g = collections.Counter(b)
        for c in g:
            if c in s:
                nb += min(s[c], g[c])
        return f'{na}A{nb}B'


s = Solution()
print(s.getHint("1122", "0001"))
