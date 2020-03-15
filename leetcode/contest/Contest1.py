class Solution:
    def luckyNumbers(self, matrix):
        m = len(matrix)
        result = []
        if m == 0:
            return result
        n = len(matrix[0])
        r, c = {}, {}
        for row in range(m):
            r[row] = 0
            _min = matrix[row][0]
            for i in range(n):
                if matrix[row][i] < _min:
                    r[row] = i
                    _min = matrix[row][i]
        for col in range(n):
            c[col] = 0
            _max = matrix[0][col]
            for i in range(m):
                if matrix[i][col] > _max:
                    c[col] = i
                    _max = matrix[i][col]
        for row in r:
            col = r[row]
            if c[col] == row:
                result.append(matrix[row][col])
        return result

s = Solution()
print(s.luckyNumbers([[1,10,4,2],
                      [9,3,8,7],
                    [15,16,17,12]]))