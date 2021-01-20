import string


class Solution:
    def countOfAtoms1(self, formula: str) -> str:
        def split(s):
            j = len(s) - 1
            while j > 0 and s[j] in string.digits:
                j -= 1
            m = 1 if j == len(s) - 1 else int(s[j + 1:])
            return s[:j + 1], m

        def getClosed(s):
            stack = []
            dClosed = {}
            for i in range(len(s)):
                if s[i] == '(':
                    stack.append(i)
                elif s[i] == ")":
                    dClosed[stack.pop()] = i
            return dClosed

        def help(f):
            f += "H"
            n = len(f)
            closed = getClosed(f)
            d = {}
            i = 0
            pre = -1
            while i < n:
                if f[i] == "(":
                    if pre != -1:
                        name, count = split(f[pre:i])
                        d[name] = d.get(name, 0) + count
                        pre = -1
                    j = closed[i]
                    subD = help(f[i + 1:j])
                    m = ""
                    j += 1
                    while j < n and f[j] in string.digits:
                        m += f[j]
                        j += 1
                    m = 1 if m == "" else int(m)
                    for k in subD:
                        d[k] = d.get(k, 0) + subD[k] * m
                    i = j
                else:
                    if f[i] in string.ascii_uppercase:
                        if pre != -1:
                            name, count = split(f[pre:i])
                            d[name] = d.get(name, 0) + count
                        pre = i
                    i += 1
            return d

        d = help(formula)
        ans = ""
        for k in sorted(d):
            ans += k
            if d[k] > 1:
                ans += str(d[k])
        return ans

    def countOfAtoms(self, formula: str) -> str:
        def split(s):
            j = len(s) - 1
            while j > 0 and s[j] in string.digits:
                j -= 1
            m = 1 if j == len(s) - 1 else int(s[j + 1:])
            return s[:j + 1], m

        def getClosed(s):
            stack = []
            dClosed = {}
            for i in range(len(s)):
                if s[i] == '(':
                    stack.append(i)
                elif s[i] == ")":
                    dClosed[stack.pop()] = i
            return dClosed

        def help(f, l, r):
            f += "H"
            d = {}
            i = l
            pre = -1
            while i < r:
                if f[i] == "(":
                    if pre != -1:
                        name, count = split(f[pre:i])
                        d[name] = d.get(name, 0) + count
                        pre = -1
                    j = closed[i]
                    subD = help(f, i + 1, j)
                    m = ""
                    j += 1
                    while j < r and f[j] in string.digits:
                        m += f[j]
                        j += 1
                    m = 1 if m == "" else int(m)
                    for k in subD:
                        d[k] = d.get(k, 0) + subD[k] * m
                    i = j
                else:
                    if f[i] in string.ascii_uppercase:
                        if pre != -1:
                            name, count = split(f[pre:i])
                            d[name] = d.get(name, 0) + count
                        pre = i
                    i += 1
            if pre != -1:
                name, count = split(f[pre:r])
                d[name] = d.get(name, 0) + count
            return d

        closed = getClosed(formula)
        d = help(formula, 0, len(formula))
        ans = ""
        for k in sorted(d):
            ans += k
            if d[k] > 1:
                ans += str(d[k])
        return ans


s = Solution()
print(s.countOfAtoms("Mg(OH)2"), s.countOfAtoms1("Mg(OH)2"))
print(s.countOfAtoms("K4(ON(SO3)2)2"), s.countOfAtoms1("K4(ON(SO3)2)2"))  # K4N2O14S4
print(s.countOfAtoms("((N2)3(LiN2)2)2"), s.countOfAtoms1("((N2)3(LiN2)2)2"))  # Li4N20
