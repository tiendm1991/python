from heapq import heappush as push
from heapq import heappop as pop


class Stone:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val > other.val

    def __eq__(self, other):
        return self.val == other.val

    def __str__(self):
        return str(self.val)


class Solution:
    def lastStoneWeight(self, stones) -> int:
        s = []
        for x in stones:
            push(s, Stone(x))
        while len(s) > 1:
            y = pop(s).val
            x = pop(s).val
            if y > x:
                push(s, Stone(y - x))
        if len(s) == 1:
            return s[0].val
        return 0


s = Solution()
print(s.lastStoneWeight([2, 7, 4, 1, 8, 1]))
