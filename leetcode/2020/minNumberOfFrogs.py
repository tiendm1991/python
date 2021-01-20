import collections
from datetime import datetime
from heapq import heappush as push
from heapq import heappop as pop


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        n = len(croakOfFrogs)
        if n == 0:
            return 0
        if n % 5 != 0:
            return -1
        d = {'': list(range(n // 5)), 'c': [], 'r': [], 'o': [], 'a': [], 'k': []}
        p = {'c': '', 'r': 'c', 'o': 'r', 'a': 'o', 'k': 'a'}
        result = set()
        for ch in croakOfFrogs:
            pre = p[ch]
            if len(d[pre]) == 0:
                return -1
            x = pop(d[pre])
            push(d[ch], x)
            if ch == 'k':
                pop(d[ch])
                push(d[''], x)
                result.add(x)
        if len(d['']) < n // 5:
            return -1
        return len(result)


s = Solution()
start = datetime.now()
print(s.minNumberOfFrogs("croakcrook"))
print(datetime.now() - start)
