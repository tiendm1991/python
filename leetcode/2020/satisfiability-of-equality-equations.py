class Solution:
    def equationsPossible(self, equations) -> bool:
        p = {}

        def find(c):
            if c not in p:
                p[c] = c
            if c != p[c]:
                p[c] = find(p[c])
            return p[c]

        def union(c1, c2):
            rc1, rc2 = find(c1), find(c2)
            if rc2 < rc1:
                p[rc1] = rc2
            else:
                p[rc2] = rc1

        for e in equations:
            if "==" in e:
                union(e[0], e[3])
        for e in equations:
            if "!=" in e:
                if find(e[0]) == find(e[3]):
                    return False

        return True


s = Solution()
print(s.equationsPossible(["a==b", "b!=a"]))
print(s.equationsPossible(["a==b", "b!=c", "c==a"]))
# print(s.equationsPossible(["e==e", "d!=e", "c==d", "d!=e"]))
