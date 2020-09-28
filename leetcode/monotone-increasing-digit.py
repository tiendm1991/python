class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        if N < 10:
            return N
        a = [int(c) for c in str(N)]
        n = len(a)
        i = n - 2
        mask = -1
        while i >= 0:
            if a[i] > a[i + 1]:
                a[i] -= 1
                mask = i
            i -= 1
        if mask == -1:
            return N
        for j in range(mask + 1, n):
            a[j] = 9
        return int(''.join([str(x) for x in a]))


s = Solution()
print(s.monotoneIncreasingDigits(332))
print(s.monotoneIncreasingDigits(10))
print(s.monotoneIncreasingDigits(1234))
print(s.monotoneIncreasingDigits(322))
