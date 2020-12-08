class Solution:
    def snakesAndLadders(self, board) -> int:
        n = len(board)
        res = 0
        q = [1]
        visited = {1}
        while q:
            newQ = []
            for cur in q:
                if cur == n * n:
                    return res
                for x in range(cur + 1, cur + 7):
                    if x > n * n:
                        break
                    i = (x - 1) // n
                    j = (x - 1) % n
                    if i % 2 == 1:
                        j = n - 1 - j
                    if board[n - 1 - i][j] != -1:
                        x = board[n - 1 - i][j]
                    if x not in visited:
                        visited.add(x)
                        newQ.append(x)
            q = newQ
            res += 1
        return -1


s = Solution()
print(s.snakesAndLadders([[-1, 7, -1], [-1, 6, 9], [-1, -1, 2]]))
# print(s.snakesAndLadders([
#     [-1, -1, -1, -1, -1, -1],
#     [-1, -1, -1, -1, -1, -1],
#     [-1, -1, -1, -1, -1, -1],
#     [-1, 35, -1, -1, 13, -1],
#     [-1, -1, -1, -1, -1, -1],
#     [-1, 15, -1, -1, -1, -1]]))
