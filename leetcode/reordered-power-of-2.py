class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        s = set()
        for i in range(31):
            x = 1 << i
            s.add(''.join(sorted(str(x))))
        return ''.join(sorted(str(N))) in s


s = Solution()
print(s.reorderedPowerOf2(46))
