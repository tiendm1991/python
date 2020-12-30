class Solution:
    def gameOfLife_largeMem(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        newBoard = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                c = [0, 0]
                for ii in range(-1, 2):
                    for jj in range(-1, 2):
                        if ii == 0 and jj == 0:
                            continue
                        x, y = i + ii, j + jj
                        if 0 <= x < m and 0 <= y < n:
                            c[board[x][y]] += 1
                if c[1] == 3 or (board[i][j] == 1 and c[1] == 2):
                    newBoard[i][j] = 1

        for i in range(m):
            for j in range(n):
                board[i][j] = newBoard[i][j]
        print(board)

    def gameOfLife_old_new(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                board[i][j] <<= 1
        for i in range(m):
            for j in range(n):
                c = [0, 0]
                for ii in range(-1, 2):
                    for jj in range(-1, 2):
                        if ii == 0 and jj == 0:
                            continue
                        x, y = i + ii, j + jj
                        if 0 <= x < m and 0 <= y < n:
                            c[board[x][y] >> 1] += 1
                if c[1] == 3 or ((board[i][j] >> 1) == 1 and c[1] == 2):
                    board[i][j] |= 1
        for i in range(m):
            for j in range(n):
                board[i][j] &= 1

    def gameOfLife(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                c = [0, 0]
                for ii in range(-1, 2):
                    for jj in range(-1, 2):
                        if ii == 0 and jj == 0:
                            continue
                        x, y = i + ii, j + jj
                        if 0 <= x < m and 0 <= y < n:
                            c[board[x][y] & 1] += 1
                if c[1] == 3 or ((board[i][j] & 1) == 1 and c[1] == 2):
                    board[i][j] = (1 << 1) | board[i][j]
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1

        print(board)


s = Solution()
s.gameOfLife_largeMem([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]])
s.gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]])
