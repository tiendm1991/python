class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m < 3:
            return
        n = len(board[0])
        if n < 3:
            return
        visited = [[False if board[i][j] == 'O' else True for j in range(n)] for i in range(m)]
        mask, flip = {}, {}

        def dfs(r, c, count):
            if r < 0 or r >= m or c < 0 or c >= n or visited[r][c]:
                return
            if board[r][c] == 'O':
                visited[r][c] = True
                mask[(r, c)] = count
                if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                    flip[count] = 'O'
            dfs(r - 1, c, count)
            dfs(r + 1, c, count)
            dfs(r, c - 1, count)
            dfs(r, c + 1, count)

        count = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    count += 1
                    flip[count] = 'X'
                    dfs(i, j, count)
        for c in mask:
            board[c[0]][c[1]] = flip[mask[c]]
        return


s = Solution()
board = [["X", "O", "O", "X", "X", "X", "O", "X", "O", "O"],
         ["X", "O", "X", "X", "X", "X", "X", "X", "X", "X"],
         ["X", "X", "X", "X", "O", "X", "X", "X", "X", "X"],
         ["X", "O", "X", "X", "X", "O", "X", "X", "X", "O"],
         ["O", "X", "X", "X", "O", "X", "O", "X", "O", "X"],
         ["X", "X", "O", "X", "X", "O", "O", "X", "X", "X"],
         ["O", "X", "X", "O", "O", "X", "O", "X", "X", "O"],
         ["O", "X", "X", "X", "X", "X", "O", "X", "X", "X"],
         ["X", "O", "O", "X", "X", "O", "X", "X", "O", "O"],
         ["X", "X", "X", "O", "O", "X", "O", "X", "X", "O"]]
s.solve(board)
print(board)
