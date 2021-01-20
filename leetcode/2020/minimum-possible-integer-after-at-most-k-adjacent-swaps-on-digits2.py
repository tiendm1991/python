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


class Solution:
    def minInteger(self, num: str, k: int) -> str:
        a = [int(c) for c in num]
        n = len(a)
        if k >= (n - 1) * n // 2:
            return ''.join([str(x) for x in sorted(a)])

        tree = SegmentTree(a)
        # print(tree.getMin(0, 0, n-1, 4, 6))
        i = 0
        result = []
        while i < n and k > 0:
            idx = tree.getMin(0, 0, n - 1, i + 1, i + k)
            if idx > -1 and a[idx] < a[i]:
                tmp = a[idx]
                for j in range(idx, i, -1):
                    a[j] = a[j - 1]
                a[i] = tmp
                tree = SegmentTree(a)
                k -= idx - i
            i += 1

        return ''.join([str(x) for x in a])


s = Solution()
print(s.minInteger("3142", 4))
# print(s.minInteger("4321", 4))
# print(s.minInteger("9000900", 3))
# print(s.minInteger("9438957234785635408", 23))
