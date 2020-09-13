class Solution:
    def insert(self, intervals, newInterval):
        if len(intervals) == 0 or newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        if intervals[-1][1] < newInterval[0]:
            return intervals + [newInterval]
        ans = []
        i = 0
        while intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1
        start = min(intervals[i][0], newInterval[0])
        while i < len(intervals) and intervals[i][1] < newInterval[1]:
            i += 1
        if i == len(intervals):
            ans.append([start, newInterval[1]])
        elif intervals[i][0] > newInterval[1]:
            ans.append([start, newInterval[1]])
            ans += intervals[i:]
        else:
            ans.append([start, intervals[i][1]])
            ans += intervals[i + 1:]
        return ans


s = Solution()
print(s.insert([[1, 5]],
               [2, 7]))
