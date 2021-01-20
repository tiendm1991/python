import collections
from heapq import heappop
from heapq import heappush


class Task:
    def __init__(self, name, remain):
        self.name = name
        self.remain = remain

    def __lt__(self, other):
        if other.remain != self.remain:
            return other.remain < self.remain
        return self.name < other.name

    def __str__(self):
        return f'{self.name}-{self.remain}'


class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        d = collections.Counter(tasks)
        q = []
        for t in d:
            heappush(q, Task(t, d[t]))
        count = 0
        while q:
            task = heappop(q)
            count += 1
            task.remain -= 1
            count += min(len(q), n)
            add = n - min(len(q), n)
            next = []
            for i in range(min(len(q), n)):
                t = heappop(q)
                t.remain -= 1
                if t.remain > 0:
                    next.append(t)
            for t in next:
                heappush(q, t)
            if task.remain > 0:
                count += add
                heappush(q, task)
        return count
