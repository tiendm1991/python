from datetime import datetime


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def calPermutation(n):
            s = 1
            for i in range(2, n + 1):
                s *= i
            return s

        result = ''
        _set = {i for i in range(1, n+1)}
        while len(result) < n:
            a = calPermutation(n - len(result) - 1)
            x = k // a if k % a == 0 else k // a + 1
            count = 1
            for c in _set:
                if count == x:
                    result += str(c)
                    _set.remove(c)
                    break
                count += 1
            k = k % a if k % a != 0 else a
        return result


s = Solution()
start = datetime.now()
print(s.getPermutation(4,9))
print(datetime.now() - start)

