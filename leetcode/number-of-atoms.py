import string


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def help(f):
            f += "H"
            n = len(f)
            d = {}
            i = 0
            pre = -1
            while i < n:
                if f[i] == "(":
                    if pre != -1:
                        s = f[pre:i]
                        j = len(s) - 1
                        while j > 0 and s[j] in string.digits:
                            j -= 1
                        m = 1 if j == len(s) - 1 else int(s[j + 1:])
                        d[s[:j + 1]] = m
                        pre = -1
                    start = i + 1
                    j = n - 1
                    while j > i and f[j] != ")":
                        j -= 1
                    subD = help(f[start:j])
                    j += 1
                    m = ""
                    while j < n and f[j] in string.digits:
                        m += f[j]
                        j += 1
                    m = 1 if m == "" else int(m)
                    for k in subD:
                        d[k] = d.get(k, 0) + subD[k] * m
                else:
                    if f[i] not in string.ascii_uppercase:
                        i += 1
                        continue
                    if pre == -1:
                        pre = i
                        i += 1
                    else:
                        s = f[pre:i]
                        j = len(s) - 1
                        while j >= 0 and s[j] in string.digits:
                            j -= 1
                        m = 1 if j == len(s) - 1 else int(s[j + 1:])
                        d[s[:j + 1]] = m
                        pre = i
                        i += 1
            return d

        d = help(formula)
        return d


s = Solution()
print(s.countOfAtoms("K4(ON(SO3)2)2"))
