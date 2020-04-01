class Solution:
    def nextGreaterElement(self, n: int) -> int:
        _max = 2 ** 31 - 1
        s = [int(c) for c in str(n)]
        stack = []
        while s:
            if not stack or s[-1] >= stack[-1]:
                stack.append(s.pop())
            else:
                j = len(stack) - 1
                while j >= 0 and stack[j] > s[-1]:
                    j -= 1
                s[-1], stack[j + 1] = stack[j + 1], s[-1]
                s += stack
                x = int(''.join([str(c) for c in s]))
                return x if x <= _max else -1
        return -1
