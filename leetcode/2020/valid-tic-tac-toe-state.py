class Solution:
    def validTicTacToe(self, board) -> bool:
        c1, c2 = 0, 0
        xxx, ooo = "XXX", "OOO"
        w1, w2 = 0, 0
        d1, d2 = "", ""
        for i in range(3):
            if board[i] == xxx:
                w1 += 1
            elif board[i] == ooo:
                w2 += 1
            s = ""
            d1 += board[i][i]
            d2 += board[i][2 - i]
            for j in range(3):
                if board[i][j] == 'X':
                    c1 += 1
                elif board[i][j] == 'O':
                    c2 += 1
                s += board[j][i]
            if s == xxx:
                w1 += 1
            elif s == ooo:
                w2 += 1
        if d1 == xxx or d2 == xxx:
            w1 += 1
        if d1 == ooo or d2 == ooo:
            w2 += 1
        if w1 * w2 > 0 or w1 + w2 > 2:
            return False
        if c1 - c2 < 0 or c1 - c2 > 1:
            return False
        if w1 > 0:
            return c1 - c2 == 1
        if w2 > 0:
            return c1 - c2 == 0
        return 0 <= c1 - c2 <= 1


s = Solution()
print(s.validTicTacToe(["XXX",
                        "XOO",
                        "OO "]))
