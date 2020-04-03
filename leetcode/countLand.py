class Region:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.s = (c - a) * (d - b)
        self.isLand = False
        self.children = []
    def __str__(self):
        return '{},{} - {},{} - {}'.format(self.a, self.b, self.c, self.d, self.isLand)

class Solution:
    def __init__(self):
        self.count = 0
        self.root = Region(0, 0, 1000, 1000)

    def buildTree(self, ls):
        # check x in y
        def checkInner(x: Region, y: Region):
            return x.a > y.a and x.b > y.b and x.c < y.c and x.d < y.d

        def add(current: Region, parent: Region):
            if parent.children:
                for node in parent.children:
                    if checkInner(current, node):
                        add(current, node)
                        return
            if not parent.isLand:
                current.isLand = not parent.isLand
                self.count += 1
            parent.children.append(current)
            return

        for region in ls:
            add(region, self.root)
        return

    def countLand(self, ls):
        regions = sorted([Region(a[0], a[1], a[2], a[3]) for a in ls], key=lambda r: r.s, reverse=True)
        self.buildTree(regions)
        return self.count


s = Solution()
print(s.countLand([[1.0, 1.0, 10.0, 6.0],
                   [1.5, 1.5, 6.0, 5.0],
                   [2.0, 2.0, 3.0, 3.0],
                   [2.0, 3.5, 3.0, 4.5],
                   [3.5, 2.0, 5.5, 4.5],
                   [4.0, 3.5, 5.0, 4.0],
                   [4.0, 2.5, 5.0, 3.0],
                   [7.0, 3.0, 9.5, 5.5],
                   [7.5, 4.0, 8.0, 5.0],
                   [8.5, 3.5, 9.0, 4.5],
                   [3.0, 7.0, 8.0, 10.0],
                   [5.0, 7.5, 7.5, 9.5],
                   [5.5, 8.0, 6.0, 9.0],
                   [6.5, 8.0, 7.0, 9.0]]))
