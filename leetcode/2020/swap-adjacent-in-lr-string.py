class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        a = [c for c in start]
        b = [c for c in end]
        n = len(a)
        i, j = 0, 0
        while i < n and j < n:
            if a[i] == 'X':
                i += 1
            elif b[j] == 'X':
                j += 1
            elif a[i] != b[j]:
                return False
            elif a[i] == 'L' and i < j:
                return False
            elif a[i] == 'R' and i > j:
                return False
            else:
                i += 1
                j += 1
        while i < n:
            if a[i] != 'X':
                return False
            i += 1
        while j < n:
            if b[j] != 'X':
                return False
            j += 1
        return True


s = Solution()
print(s.canTransform("RXXLRXRXL",
                     "XRLXXRRLX"))
print(s.canTransform("LXXLXRLXXL",
                     "XLLXRXLXLX"))
