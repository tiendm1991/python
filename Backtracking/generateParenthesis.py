from datetime import datetime


class Solution:
    def generateParenthesis(self, n: int):
        result = []
        self.generate(n, result, '', 0, 0)
        return result
    def generate(self, n, result, s, left, right):
        if len(s) == 2*n and s not in result:
            result.append(s)
            return
        if left < n:
            self.generate(n, result, s + '(', left+1, right)
        if left > right:
            self.generate(n, result, s + ')', left, right + 1)
        return

s = Solution()
start = datetime.now()
print(s.generateParenthesis(3))
print(datetime.now() - start)

