class SegmentTree:
    def __init__(self, arr):
        self.maxInt = 10 ** 9
        self.st = [self.maxInt] * 4 * len(arr)
        for i, v in enumerate(arr):
            self.update(0, 0, len(arr) - 1, i, v)

    def update(self, id, left, right, i, val):
        if i < left or i > right:
            return
        if left == right:
            self.st[id] = val
            return
        mid = (left + right) // 2
        self.update(id * 2 + 1, left, mid, i, val)
        self.update(id * 2 + 2, mid + 1, right, i, val)
        self.st[id] = min(self.st[id * 2 + 1], self.st[id * 2 + 2])

    def getMin(self, id, left, right, u, v):
        if u > right or v < left:
            return self.maxInt
        if u <= left and v >= right:
            return self.st[id]
        mid = (left + right) // 2
        minLeft = self.getMin(id * 2 + 1, left, mid, u, v)
        minRight = self.getMin(id * 2 + 2, mid + 1, right, u, v)
        return min(minLeft, minRight)
