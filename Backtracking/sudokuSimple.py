class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board, 0, 0)

    def solve(self, board, i, j):
        if i == 9:
            return True
        if j == 9:
            return self.solve(board, i + 1, 0)
        if board[i][j] != '.':
            return self.solve(board, i, j + 1)
        else:
            for x in range(1, 10):
                board[i][j] = str(x)
                if self.isValidSudoku(board):
                    check = self.solve(board, i, j + 1)
                    if check:
                        return True
                board[i][j] = '.'
        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            check, check2 = [False] * 9, [False] * 9
            for j in range(9):
                c = board[i][j]
                if c != '.':
                    x = int(c)
                    if check[x - 1]:
                        return False
                    check[x - 1] = True
                c = board[j][i]
                if c != '.':
                    y = int(c)
                    if check2[y - 1]:
                        return False
                    check2[y - 1] = True
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                check = [False] * 9
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        c = board[k][l]
                        if c != '.':
                            x = int(c)
                            if check[x - 1]:
                                return False
                            check[x - 1] = True
        return True


s = Solution()
a = [[".", ".", "9", "7", "4", "8", ".", ".", "."], ["7", ".", ".", ".", ".", ".", ".", ".", "."],
     [".", "2", ".", "1", ".", "9", ".", ".", "."], [".", ".", "7", ".", ".", ".", "2", "4", "."],
     [".", "6", "4", ".", "1", ".", "5", "9", "."], [".", "9", "8", ".", ".", ".", "3", ".", "."],
     [".", ".", ".", "8", ".", "3", ".", "2", "."], [".", ".", ".", ".", ".", ".", ".", ".", "6"],
     [".", ".", ".", "2", "7", "5", "9", ".", "."]]
start = datetime.now()
s.solveSudoku(a)
print(a)
print(datetime.now() - start)
