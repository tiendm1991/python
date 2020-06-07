import functools
class Solution:
    def getStrongest(self, arr, k: int):
        arr.sort()
        n = len(arr)
        m = arr[(n-1) // 2]
        def cmp(x1, x2):
            if abs(x1-m) != abs(x2 - m):
                return abs(x1-m) - abs(x2-m)
            return x1 - x2
        a = sorted(arr, key=functools.cmp_to_key(cmp), reverse=True)
        return a[:k]

s = Solution()
print(s.getStrongest([1,2,3,4,5], 2))