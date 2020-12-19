import collections


class Solution:
    def movesToStamp(self, stamp: str, target: str):
        n = len(target)
        m = len(stamp)
        t = "*" * n
        stop = "*" * m

        def check(a, idx):
            for i in range(m):
                if a[idx + i] != '*' and a[idx + i] != stamp[i]:
                    return False
            return True

        visited = set()

        def backtrack(cur, res):
            if cur in visited:
                return ""
            if cur == t:
                return res
            candidate = set()
            for i in range(n - m + 1):
                if check(cur, i):
                    candidate.add(i)
            if candidate:
                x = cur
                y = res
                for i in candidate:
                    if x[i: i + m] != stop:
                        x = x[:i] + stop + x[i + m:]
                        y += "-" + str(i)
                if x == cur:
                    visited.add(x)
                    return ""
                rx = backtrack(x, y)
                if rx:
                    return rx
                else:
                    visited.add(x)
                    return ""
            visited.add(cur)
            return ""

        r = backtrack(target, "")
        return [] if r == '' else [int(c) for c in r.strip("-").split("-")][::-1]


s = Solution()
print(s.movesToStamp("qxq", "qxqxqxqqxqxqqxqxqxqqxqxqqqxqqxqqqxqqxxqxqqxqqqxqqq"))
# print(s.movesToStamp("by", "bbybyybyby"))
# print(s.movesToStamp("o", "oooooooooo"))
# print(s.movesToStamp("abca", "aabcaca"))
# print(s.movesToStamp("abc", "ababc"))
# print(s.movesToStamp("aye", "eyeye"))
