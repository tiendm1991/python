import math
class Solution:
    def sumFourDivisors(self, nums) -> int:
        def valid(x):
            s = set()
            for i in range(1, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    s.add(i)
                    s.add(x // i)
                    if i == x // i:
                        return 0
            return 0 if len(s) != 4 else sum(s)
        s = 0
        for x in nums:
            s += valid(x)
        return s
s = Solution()
print(s.sumFourDivisors([1,2,3,4,5,6,7,8,9,10]))