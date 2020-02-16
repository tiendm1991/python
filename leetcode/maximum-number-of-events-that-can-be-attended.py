class Solution:
    def maxEvents(self, events) -> int:
        events = sorted(events, key=lambda x: x[1] * 10 + x[0])
        _maxD = events[-1][1]
        visited = [0] * len(events)
        used = [False] * (_maxD + 1)
        start = 1
        for i in range(len(events)):
            for d in range(events[i][0], events[i][1] + 1):
                if not used[d] and d >= events[i][0] and d <= events[i][1]:
                    visited[i] = d
                    used[d] = True
                    break
        return len([x for x in visited if x > 0])