import math


class TreeAncestor:

    def __init__(self, n: int, parent):
        self.ln = math.ceil(math.log2(n))
        self.dp = [[-1 for j in range(self.ln + 1)] for i in range(n)]
        for i in range(1, n):
            for j in range(self.ln + 1):
                if j == 0:
                    self.dp[i][j] = parent[i]
                else:
                    self.dp[i][j] = self.dp[self.dp[i][j - 1]][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        while k > 0 and node != -1:
            x = int(math.log2(k))
            node = self.dp[node][x]
            k -= 2 ** x
        return node


# Your TreeAncestor object will be instantiated and called as such:
obj = TreeAncestor(14, [-1, 0, 0, 1, 1, 2, 2, 4, 7, 8, 9, 9, 10, 12])
print(obj.getKthAncestor(13, 7))
