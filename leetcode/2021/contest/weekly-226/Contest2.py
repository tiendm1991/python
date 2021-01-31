import collections


class Solution:
    def restoreArray(self, adjacentPairs):
        d = {}
        for p in adjacentPairs:
            if p[0] not in d:
                d[p[0]] = [p[1]]
            else:
                d[p[0]].append(p[1])
            if p[1] not in d:
                d[p[1]] = [p[0]]
            else:
                d[p[1]].append(p[0])
        start = None
        for i in d:
            if len(d[i]) == 1:
                start = i
                break
        res = [start]
        for i in range(len(d) - 1):
            cur = res[-1]
            res.append(d[cur][0])
            if cur in d[res[-1]]:
                d[res[-1]].remove(cur)
        return res


s = Solution()
print(s.restoreArray([[4, -2], [1, 4], [-3, 1]]))
