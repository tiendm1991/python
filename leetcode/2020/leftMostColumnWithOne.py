from datetime import datetime


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
class BinaryMatrix():
    def __init__(self, a):
        self.a = a

    def get(self, x: int, y: int) -> int:
        return self.a[x][y]

    def dimensions(self):
        return [len(self.a), len(self.a[0])]


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        d = binaryMatrix.dimensions()
        nRows, nCols = d[0], d[1]
        _min = nCols

        def binarySearch(row, colStart, colEnd):
            if colStart > colEnd:
                return nCols
            if colStart == colEnd:
                return colStart if binaryMatrix.get(row, colStart) == 1 else nCols
            colMid = (colStart + colEnd) // 2
            if binaryMatrix.get(row, colMid) == 1:
                return binarySearch(row, colStart, colMid)
            else:
                return binarySearch(row, colMid + 1, colEnd)

        for row in range(nRows):
            _min = min(_min, binarySearch(row, 0, nCols - 1))
        return _min if _min < d[1] else -1


s = Solution()
startTime = datetime.now()
print(s.leftMostColumnWithOne(BinaryMatrix([[0, 0, 0, 1],
                                            [0, 0, 1, 1],
                                            [0, 1, 1, 1]])))
print(datetime.now() - startTime)
