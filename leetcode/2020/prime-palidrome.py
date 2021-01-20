class Solution:
    def primePalindrome(self, n: int) -> int:
        def isPrime(x):
            if x < 2:
                return False
            if x == 2 or x == 3:
                return True
            if x % 2 == 0:
                return False
            i = 3
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 2
            return True

        if n <= 2:
            return 2
        if n == 3:
            return 3
        if 8 <= n <= 11:
            return 11

        for i in range(1, 10 ** 5):
            s = str(i)
            s += s[-2::-1]
            x = int(s)
            if isPrime(x) and s >= n:
                return x
        return -1
