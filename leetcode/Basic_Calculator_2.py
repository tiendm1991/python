class Solution:
    def calculate(self, s: str) -> int:
        def multy(a):
            b = a.replace("/", "*/").split("*")
            ans = 1
            for y in b:
                if not y.startswith("/"):
                    ans *= int(y)
                else:
                    ans //= int(y[1:])
            return ans

        s = s.strip().replace("-", "+-").replace(" ", "")
        stack = s.split("+")
        res = 0
        for x in stack:
            if "-" not in x and "*" not in x and "/" not in x:
                res += int(x)
            elif x.startswith("-"):
                res -= multy(x[1:])
            else:
                res += multy(x)
        return res


s = Solution()
print(s.calculate(" 3+5 / 2 - 7 / 3"))
