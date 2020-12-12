class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        stack = []
        res = 0
        for c in S:
            if c == '0' and stack and stack[-1] == '1':
                stack.pop()
                res += 1
            else:
                stack.append(c)
        return res

    def minFlipsMonoIncr2(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 0
        a, b = [0] * n, [0] * n
        _max = 0
        a[0] = 1 if s[0] == '0' else 0
        for i in range(1, n):
            a[i] = a[i - 1]
            if s[i] == '0':
                a[i] += 1
        for i in range(n - 1, -1, -1):
            if i < n - 1:
                b[i] = b[i + 1]
            if s[i] == '1':
                b[i] += 1
            _max = max(_max, a[i] + b[i])
        return n - _max


s = Solution()
print(s.minFlipsMonoIncr("00011000"), s.minFlipsMonoIncr2("00011000"))
