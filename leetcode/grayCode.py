from datetime import datetime


class Solution:
    def grayCode(self, n: int):
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        result = [0, 1]
        for i in range(2, n+1):
            plus = pow(2, i-1)
            extend = list(map(lambda x: x+plus, result[::-1]))
            result += extend
        return result


s = Solution()
start = datetime.now()
print(s.grayCode(3))
print(datetime.now() - start)

