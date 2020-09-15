class Solution:
    def maximumSwap1(self, num: int) -> int:
        if num < 10:
            return num
        s = [c for c in str(num)]
        n = len(s)
        stack = []
        x, y = 0, 0
        for i in range(n):
            if not stack or s[stack[-1]] >= s[i]:
                stack.append(i)
            else:
                y = i
                break
        if len(stack) == n:
            return num
        for i in range(y, n):
            if s[i] >= s[y]:
                y = i
        while stack and s[y] > s[stack[-1]]:
            x = stack.pop()
        s[x], s[y] = s[y], s[x]
        return int(''.join(s))

    def maximumSwap(self, num: int) -> int:
        if num < 10:
            return num
        s = [c for c in str(num)]
        n = len(s)
        d = {int(s[i]): i for i in range(n)}
        for i in range(n):
            for j in range(9, int(s[i]), -1):
                if j in d and d[j] > i:
                    s[i], s[d[j]] = s[d[j]], s[i]
                    return int(''.join(s))
        return num


s = Solution()
print(s.maximumSwap(43456))
