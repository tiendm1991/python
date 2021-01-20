import collections


class Solution:
    def isNStraightHand(self, a, w: int) -> bool:
        n = len(a)
        if n % w != 0:
            return False
        d = collections.Counter(a)
        m = n // w
        sub = [[] for i in range(m)]
        for k in sorted(d):
            if d[k] > m:
                return False
            for i in range(m):
                if d[k] == 0:
                    break
                if len(sub[i]) == w:
                    continue
                if len(sub[i]) == 0 or sub[i][-1] + 1 == k:
                    sub[i].append(k)
                    d[k] -= 1
            if d[k] > 0:
                return False
        return True


s = Solution()
# print(s.isNStraightHand([1, 1, 2, 2, 3, 3], 2))
print(s.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))
