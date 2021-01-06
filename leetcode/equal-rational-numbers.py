class Solution:
    def isRationalEqual(self, S: str, T: str) -> bool:
        progression = [10 ** i for i in range(0, -5, -1)]
        epsilon = 10 ** (-9)

        def parse(s):
            if '(' not in s:
                return float(s)
            open = s.index('(')
            dot = s.index('.')
            repeat = s[open + 1: -1]
            p = progression[len(repeat)]
            # a = float(s[:dot + 1] + '0' * (open - dot - 1) + repeat)
            a = float(repeat) * 10 ** (dot + 1 - open - len(repeat))
            res = float(s[:open]) + a / (1 - p)
            return res

        return abs(parse(S) - parse(T)) < epsilon


s = Solution()
print(s.isRationalEqual("0.1666(6)", "0.166(66)"))
