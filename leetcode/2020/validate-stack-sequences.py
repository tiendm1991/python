class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        n = len(pushed)
        stack = []
        i, j = 0, 0
        while i < n:
            while not stack or stack[-1] != popped[i]:
                if j == n:
                    return False
                stack.append(pushed[j])
                j += 1
            stack.pop()
            i += 1
        return True


s = Solution()
print(s.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
print(s.validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
