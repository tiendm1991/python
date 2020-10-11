class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if query_row == 0:
            return min(1, poured)
        ans = [poured]
        for i in range(1, query_row + 1):
            a = [0] * (i + 1)
            a[0] = max((ans[0] - 1), 0) / 2
            a[i] = max((ans[-1] - 1), 0) / 2
            for j in range(1, i):
                a[j] = (max(ans[j - 1] - 1, 0) + max(ans[j] - 1, 0)) / 2
            ans = a
        return min(ans[query_glass], 1)


s = Solution()
print(s.champagneTower(13, 4, 1))
print(s.champagneTower(20, 5, 1))
print(s.champagneTower(19, 5, 1))
print(s.champagneTower(25, 6, 1))
print(s.champagneTower(100000009, 33, 17))
