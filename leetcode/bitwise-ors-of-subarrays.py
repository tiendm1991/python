class Solution:
    def subarrayBitwiseORs(self, a) -> int:
        n = len(a)
        if n == 1:
            return 1
        cur = {a[0]}
        res = {a[0]}
        for i in range(1, n):
            x = a[i]
            newCur = {x}
            for y in cur:
                newCur.add(x | y)
            res |= newCur
            cur = newCur
        return len(res)


s = Solution()
print(s.subarrayBitwiseORs([11, 2, 8, 3]))
print(s.subarrayBitwiseORs([1, 2, 4]))
print(s.subarrayBitwiseORs([1, 2]))
