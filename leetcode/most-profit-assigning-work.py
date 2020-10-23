import heapq


class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker) -> int:
        n = len(worker)
        ans = 0
        worker.sort()
        a = [[difficulty[i], -profit[i]] for i in range(n)]
        a.sort()
        h = []
        i, j = 0, 0
        while i < n and worker[i] < a[j][0]:
            i += 1
        if i == n:
            return 0
        while i < n:
            while j < len(a) and a[j][0] <= worker[i]:
                heapq.heappush(h, a[j][1])
                j += 1
            ans += -h[0]
            i += 1
        return ans


s = Solution()
print(s.maxProfitAssignment([13, 37, 58],
                            [4, 90, 96],
                            [34, 45, 73]))
print(s.maxProfitAssignment([30, 30, 57],
                            [24, 66, 99],
                            [25, 25, 40]))
print(s.maxProfitAssignment([2, 4, 6, 8, 10],
                            [10, 20, 30, 40, 50],
                            [4, 5, 6, 7]))
