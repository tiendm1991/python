class Solution:
    def minimumDeletions1(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 0
        m = 0
        a = [0] * n
        a[0] = 1 if s[0] == 'a' else 0
        for i in range(1, n):
            a[i] = a[i - 1]
            if s[i] == 'a':
                a[i] += 1
        b = 1 if s[-1] == 'b' else 0
        m = a[-1] + b
        for i in range(n - 2, -1, -1):
            if s[i] == 'b':
                b += 1
            m = max(m, a[i] + b)
        return n - m

    def minimumDeletions(self, s: str) -> int:
        stack = []
        res = 0
        for c in s:
            if stack and c < stack[-1]:
                stack.pop()
                res += 1
            else:
                stack.append(c)
        return res


s = Solution()
print(s.minimumDeletions("aabbabaabb"))
# print(s.minimumDeletions("aabbabb"))
# print(s.minimumDeletions("abaabaaaabaa"))
# print(s.minimumDeletions("aaaaaaaaaaaaaa"))
# print(s.minimumDeletions("aababbab"))
