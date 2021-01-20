class Solution:
    def minDeletionSize(self, a) -> int:
        m, n = len(a), len(a[0])
        res = 0
        pre = [''] * m
        for j in range(n):
            check = pre[::]
            check[0] += a[0][j]
            isDelete = False
            for i in range(1, m):
                check[i] += a[i][j]
                if check[i] < check[i - 1]:
                    res += 1
                    isDelete = True
                    break
            if not isDelete:
                if len(set(check)) == m:
                    return res
                else:
                    pre = check
        return res


s = Solution()
print(s.minDeletionSize(["xga", "xfb", "yfa"]))
print(s.minDeletionSize(["ca", "bb", "ac"]))
print(s.minDeletionSize(["xc", "yb", "za"]))
print(s.minDeletionSize(["zyx", "wvu", "tsr"]))
