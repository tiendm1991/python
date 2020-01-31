from datetime import datetime


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def calPermutation(n):
            s = 1
            for i in range(2, n + 1):
                s *= i
            return s

        result = ''
        while len(result) < n:
            a = calPermutation(n - len(result) - 1)
            x = k // a if k % a == 0 else k // a + 1
            count, c = 0, 0
            while count < x:
                c += 1
                if str(c) not in result:
                    count += 1
            result += str(c)
            k = k % a if k % a != 0 else a
        return result


s = Solution()
start = datetime.now()
print(s.getPermutation(4,9))
print(datetime.now() - start)

