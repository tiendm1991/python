class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.st = [-1] * 4 * len(arr)
        for i, v in enumerate(arr):
            self.update(0, 0, len(arr) - 1, i)

    def update(self, id, left, right, i):
        if i < left or i > right:
            return
        if left == right:
            self.st[id] = i
            return
        mid = (left + right) // 2
        self.update(id * 2 + 1, left, mid, i)
        self.update(id * 2 + 2, mid + 1, right, i)
        idLeft = self.st[id * 2 + 1]
        idRight = self.st[id * 2 + 2]
        if idLeft == -1 and idRight == -1:
            return
        elif idRight == -1:
            self.st[id] = idLeft
        elif idLeft == -1:
            self.st[id] = idRight
        else:
            self.st[id] = idLeft if self.arr[idLeft] <= self.arr[idRight] else idRight

    def getMin(self, id, left, right, u, v):
        if u > right or v < left:
            return -1
        if u <= left and v >= right:
            return self.st[id]
        mid = (left + right) // 2
        idLeft = self.getMin(id * 2 + 1, left, mid, u, v)
        idRight = self.getMin(id * 2 + 2, mid + 1, right, u, v)
        if idLeft == -1 and idRight == -1:
            return -1
        elif idRight == -1:
            return idLeft
        elif idLeft == -1:
            return idRight
        else:
            return idLeft if self.arr[idLeft] <= self.arr[idRight] else idRight


a = [9, 4, 3, 8, 9, 5, 7, 2, 3, 4, 7, 8, 5, 6, 3, 5, 4, 0, 8]
tree = SegmentTree(a)
print(tree.getMin(0, 0, len(a) - 1, 4, 6))
print(tree.getMin(0, 0, len(a) - 1, 2, 10))
print(tree.getMin(0, 0, len(a) - 1, 5, 17))
