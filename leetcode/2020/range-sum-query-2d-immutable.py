class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r = len(matrix)
        c = 0
        if r != 0:
            c = len(matrix[0])
        self.m = [[0 for j in range(c + 1)] for i in range(r + 1)]
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                self.m[i][j] = self.m[i - 1][j] + self.m[i][j - 1] - self.m[i - 1][j - 1] + matrix[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.m:
            return None
        return self.m[row2 + 1][col2 + 1] - self.m[row2 + 1][col1] - self.m[row1][col2 + 1] + self.m[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
