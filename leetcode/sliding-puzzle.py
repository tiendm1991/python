class Solution:
    def slidingPuzzle(self, board) -> int:
        target = ((1, 2, 3), (4, 5, 0))
        x, y = -1, -1
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    x, y = i, j
        a = tuple(tuple(b) for b in board)
        if a == target:
            return 0
        start = [a, x, y]
        visited = {a}
        q = [start]
        ans = 0
        while q:
            newQ = []
            ans += 1
            for p in q:
                t, i, j = [list(x) for x in p[0]], p[1], p[2]
                for ii in range(-1, 2):
                    for jj in range(-1, 2):
                        if ii * jj != 0 or not (0 <= i + ii < 2 and 0 <= j + jj < 3):
                            continue
                        t[i + ii][j + jj], t[i][j] = t[i][j], t[i + ii][j + jj]
                        new = tuple(tuple(b) for b in t)
                        if new == target:
                            return ans
                        if new not in visited:
                            newQ.append([new, i + ii, j + jj])
                            visited.add(new)
                        t[i + ii][j + jj], t[i][j] = t[i][j], t[i + ii][j + jj]
            q = newQ
        return -1


s = Solution()
print(s.slidingPuzzle([[4, 1, 2], [5, 0, 3]]))
