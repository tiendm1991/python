class Solution:
    def minSwapsCouples(self, row) -> int:
        n = len(row)
        p = {row[i]: i for i in range(n)}
        ans = 0
        for i in range(0, n, 2):
            couple = i + 1
            pos = p[i]
            posCouple = p[couple]
            if pos % 2 == 0:
                posNeighbor, neighbor = pos + 1, row[pos + 1]
                if posCouple != pos + 1:
                    ans += 1
                    p[neighbor], p[couple] = posCouple, posNeighbor
                    row[posNeighbor], row[posCouple] = couple, neighbor
            else:
                posNeighbor, neighbor = pos - 1, row[pos - 1]
                if posCouple != pos - 1:
                    ans += 1
                    p[neighbor], p[couple] = posCouple, posNeighbor
                    row[posNeighbor], row[posCouple] = couple, neighbor
        return ans


s = Solution()
print(s.minSwapsCouples([5, 2, 3, 0, 4, 1]))
