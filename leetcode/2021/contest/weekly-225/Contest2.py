import collections
import string


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        ca, cb = collections.Counter(a), collections.Counter(b)
        c1, c2 = float("inf"), float("inf")
        for c in string.ascii_lowercase:
            if c == "a":
                continue
            rc1, rc2 = 0, 0
            for cx in string.ascii_lowercase:
                if cx >= c:
                    rc1 += ca.get(cx, 0)
                else:
                    rc2 += ca.get(cx, 0)
            for cy in string.ascii_lowercase:
                if cy < c:
                    rc1 += cb.get(cy, 0)
                else:
                    rc2 += cb.get(cy, 0)
            c1 = min(c1, rc1)
            c2 = min(c2, rc2)
        m = 0
        for c in string.ascii_lowercase:
            common = min(ca.get(c, 0), cb.get(c, 0))
            m = max(m, common)
        c3 = len(a) + len(b) - 2 * m
        return min(c1, c2, c3)


s = Solution()
print(s.minCharacters("a", "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"))
print(s.minCharacters("ukrwx", "sqjlxe"))
print(s.minCharacters("ace", "abe"))
print(s.minCharacters("bcd", "accde"))
print(s.minCharacters("abe", "ace"))
print(s.minCharacters("e", "e"))
print(s.minCharacters("da", "cced"))
print(s.minCharacters("aba", "caa"))
