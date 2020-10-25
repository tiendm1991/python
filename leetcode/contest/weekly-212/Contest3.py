import heapq


class Solution:
    def minimumEffortPath(self, heights) -> int:
        m = len(heights)
        n = len(heights[0])
        if m == 1 and n == 1:
            return 0
        q = []
        if m > 1:
            heapq.heappush(q, [abs(heights[1][0] - heights[0][0]), 1, 0])
        if n > 1:
            heapq.heappush(q, [abs(heights[0][1] - heights[0][0]), 0, 1])
        ans = 0
        heapq.heapify(q)
        visited = [[False for j in range(n)] for i in range(m)]
        while q:
            t = heapq.heappop(q)
            ans = max(ans, t[0])
            if visited[t[1]][t[2]]:
                continue
            visited[t[1]][t[2]] = True
            if t[1] == m - 1 and t[2] == n - 1:
                return ans
            if 0 <= t[1] - 1 and not visited[t[1] - 1][t[2]]:
                heapq.heappush(q, [abs(heights[t[1] - 1][t[2]] - heights[t[1]][t[2]]), t[1] - 1, t[2]])
            if 0 <= t[2] - 1 and not visited[t[1]][t[2] - 1]:
                heapq.heappush(q, [abs(heights[t[1]][t[2] - 1] - heights[t[1]][t[2]]), t[1], t[2] - 1])
            if t[1] + 1 < m and not visited[t[1] + 1][t[2]]:
                heapq.heappush(q, [abs(heights[t[1] + 1][t[2]] - heights[t[1]][t[2]]), t[1] + 1, t[2]])
            if t[2] + 1 < n and not visited[t[1]][t[2] + 1]:
                heapq.heappush(q, [abs(heights[t[1]][t[2] + 1] - heights[t[1]][t[2]]), t[1], t[2] + 1])
        return ans


s = Solution()
print(s.minimumEffortPath([[4, 3, 4, 10, 5, 5, 9, 2],
                           [10, 8, 2, 10, 9, 7, 5, 6],
                           [5, 8, 10, 10, 10, 7, 4, 2],
                           [5, 1, 3, 1, 1, 3, 1, 9],
                           [6, 4, 10, 6, 10, 9, 4, 6]]))
print(s.minimumEffortPath([[1, 2, 1, 1, 1],
                           [1, 2, 1, 2, 1],
                           [1, 2, 1, 2, 1],
                           [1, 2, 1, 2, 1],
                           [1, 1, 1, 2, 1]]))
print(s.minimumEffortPath([[1, 2, 2],
                           [3, 8, 2],
                           [5, 3, 5]]))
print(s.minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]))
