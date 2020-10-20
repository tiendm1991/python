class Solution:
    def ambiguousCoordinates(self, S: str):
        ans = []
        s = S[1:-1]
        n = len(s)

        def help(s):
            res = []
            if int(s) == 0:
                if len(s) == 1:
                    res.append('0')
            elif s[0] == '0':
                if s[-1] != '0':
                    res.append(s[0] + '.' + s[1:])
                return res
            else:
                for i in range(1, len(s)):
                    if s[-1] != '0':
                        res.append(s[:i] + '.' + s[i:])
                res.append(s)
            return res

        for i in range(1, n):
            a = help(s[:i])
            b = help(s[i:])
            for x in a:
                for y in b:
                    ans.append(f'({x}, {y})')
        return ans


so = Solution()
print(so.ambiguousCoordinates("(0010)"))
