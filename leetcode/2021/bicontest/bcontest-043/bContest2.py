class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            s = s.replace('a', '#').replace('b', 'a').replace('#', 'b')
            x, y = y, x

        def caculateRemain(a):
            ans = 0
            stk = []
            for i, c in enumerate(a):
                if c == 'a' and stk and stk[-1] == 'b':
                    stk.pop()
                    ans += y
                else:
                    stk.append(c)
            return ans

        res = 0
        stack = []
        for i, c in enumerate(s):
            if c == 'b':
                if stack and stack[-1] == 'a':
                    stack.pop()
                    res += x
                else:
                    stack.append(c)
            elif c == 'a':
                stack.append(c)
            else:
                res += caculateRemain(stack)
                stack = []
        res += caculateRemain(stack)
        return res


s = Solution()
print(s.maximumGain("bbaa", 5, 3))
print(s.maximumGain("cabxbae", 5, 3))
print(s.maximumGain("cdbcbbaaabab", 4, 5))
# print(s.maximumGain("aabbaaxybbaabb", 5, 4))
