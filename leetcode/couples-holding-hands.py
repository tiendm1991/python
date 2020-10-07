class Solution:
    def minSwapsCouples(self, row) -> int:
        n = len(row)
        p = {row[i]: i for i in range(n)}
        ans = 0
        for i in range(0, n, 2):
            neighbor = i + 1
            pos = p[i]
            posNeighbor = p[neighbor]
            if pos % 2 == 0:
                if posNeighbor != pos + 1:
                    ans += 1
                    p[row[pos + 1]], p[neighbor] = p[neighbor], p[row[pos + 1]]
                    row[pos + 1], row[posNeighbor] = row[posNeighbor], row[pos + 1]
            else:
                if posNeighbor != pos - 1:
                    ans += 1
                    p[row[pos - 1]], p[neighbor] = p[neighbor], p[row[pos - 1]]
                    row[pos - 1], row[posNeighbor] = row[posNeighbor], row[pos - 1]
        return ans


s = Solution()
print(s.minSwapsCouples([5, 2, 3, 0, 4, 1]))
