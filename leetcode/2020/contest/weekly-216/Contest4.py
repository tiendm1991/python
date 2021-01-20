class Solution:
    def minimumEffort(self, tasks) -> int:
        ans = sum([t[0] for t in tasks])
        a = sorted(tasks, key=lambda x: x[0] - x[1])
        remain = ans
        for x in a:
            if remain < x[1]:
                ans += x[1] - remain
                remain = x[1]
            remain -= x[0]
        return ans


s = Solution()
print(s.minimumEffort([[1, 3], [2, 4], [10, 11], [10, 12], [8, 9]]))
print(s.minimumEffort([[1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 12]]))
print(s.minimumEffort([[1, 2], [2, 4], [4, 8]]))
