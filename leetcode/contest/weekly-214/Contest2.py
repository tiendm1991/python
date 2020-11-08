import collections


class Solution:
    def minDeletions(self, s: str) -> int:
        d = collections.Counter(s)
        d2 = {}
        for c in d:
            if d[c] not in d2:
                d2[d[c]] = [c]
            else:
                d2[d[c]].append(c)
        ans = 0
        while True:
            stop = True
            for x in d2:
                if len(d2[x]) > 1:
                    stop = False
                    while len(d2[x]) > 1:
                        c = d2[x].pop()
                        y = x
                        while y > 0 and y in d2:
                            y -= 1
                        if y > 0:
                            d2[y] = c
                        ans += x - y
                    break
            if stop:
                break
        return ans


s = Solution()
print(s.minDeletions("ceabaacb"))
print(s.minDeletions("aaabbbcc"))
