from datetime import datetime


class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        check = [[[False for k in range(9)] for j in range(9)] for i in range(3)]
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != '.':
                    x = int(c)
                    check[0][i][x - 1] = True
                c = board[j][i]
                if c != '.':
                    y = int(c)
                    check[1][i][y - 1] = True
        count = 0
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        c = board[k][l]
                        if c != '.':
                            x = int(c)
                            check[2][count][x - 1] = True
                count += 1
        self.solve(board, check, 0, 0)

    def solve(self, board, check, i, j):
        if i == 9:
            return True
        if j == 9:
            return self.solve(board, check, i + 1, 0)
        if board[i][j] != '.':
            return self.solve(board, check, i, j + 1)
        else:
            for x in range(1, 10):
                board[i][j] = str(x)
                if self.isValidSudoku(board, check, i, j, x):
                    self.updateStatus(check, i, j, x, True)
                    stop = self.solve(board, check, i, j + 1)
                    if stop:
                        return True
                    self.updateStatus(check, i, j, x, False)
                board[i][j] = '.'
        return False

    def isValidSudoku(self, board, check, i, j, x):
        if check[0][i][x - 1] or check[1][j][x - 1] or check[2][(i // 3) * 3 + j // 3][x - 1]:
            return False
        return True

    def updateStatus(self, check, i, j, x, b):
        check[0][i][x - 1] = b
        check[1][j][x - 1] = b
        check[2][(i // 3) * 3 + j // 3][x - 1] = b


s = Solution()
a = [["2", ".", ".", ".", ".", ".", ".", ".", "."],
     ["1", ".", "7", "4", ".", ".", ".", ".", "3"],
     ["3", ".", ".", "2", ".", ".", ".", "5", "."],
     [".", ".", "5", ".", "2", ".", ".", ".", "."],
     [".", "6", ".", "1", ".", ".", "4", ".", "."],
     [".", ".", ".", ".", ".", "7", ".", ".", "."],
     [".", ".", ".", ".", ".", "3", ".", ".", "8"],
     ["8", ".", ".", "6", ".", ".", "2", ".", "."],
     [".", "4", ".", "8", ".", ".", ".", "3", "1"]]
start = datetime.now()
s.solveSudoku(a)
print(a)
print(datetime.now() - start)
