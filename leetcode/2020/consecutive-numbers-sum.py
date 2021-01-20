class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        if n == 1:
            return 1
        ans = 0
        i = 2
        while True:
            x = (i * (i + 1)) // 2
            if n < x:
                break
            elif (n - x) % i == 0:
                ans += 1
            i += 1
        return ans + 1


s = Solution()
print(s.consecutiveNumbersSum(15))
print(s.consecutiveNumbersSum(3))
