class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        ans = []
        for i in range(left, right + 1):
            x = i
            while x > 0:
                digit = x % 10
                if digit == 0 or i % digit != 0:
                    break
                x //= 10
            if x == 0:
                ans.append(i)
        return ans


s = Solution()
print(s.selfDividingNumbers(1, 22))
