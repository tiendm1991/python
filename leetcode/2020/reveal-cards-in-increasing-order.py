import collections


class Solution:
    def deckRevealedIncreasing(self, a):
        a.sort()
        n = len(a)
        res = collections.deque()
        for i in range(n - 1, -1, -1):
            if res:
                last = res.pop()
                res.appendleft(last)
            res.appendleft(a[i])
        return list(res)


s = Solution()
print(s.deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]))  # [2, 3, 5, 7, 11, 13, 17]
