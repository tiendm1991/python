class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
        ans = 0
        for x in range(L, R + 1):
            s = bin(x)
            a = s.count("1")
            if a in primes:
                ans += 1
        return ans


s = Solution()
print(s.countPrimeSetBits(990, 1048))
