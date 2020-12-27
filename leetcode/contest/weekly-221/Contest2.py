import heapq


class Solution:
    def eatenApples(self, apples, days) -> int:
        n = len(apples)
        h = []
        res = 0
        maxDay = 0

        for i in range(n):
            maxDay = max(maxDay, i + 1 + days[i])
            heapq.heappush(h, [i + 1 + days[i], apples[i]])
        total = [0] * (maxDay + 1)
        idx = 0
        for i in range(1, maxDay + 1):
            total[i] = total[i - 1]
            if i == idx + 1 and idx < n:
                total[i] += apples[idx]
                total[i + days[idx]] -= apples[idx]
                idx += 1
        for i in range(1, maxDay + 1):
            while h and (i >= h[0][0] or h[0][1] == 0):
                heapq.heappop(h)
            if h:
                if total[i] == 0:
                    continue
                res += 1
                if h[0][1] == 1:
                    heapq.heappop(h)
                else:
                    h[0][1] -= 1
        return res


s = Solution()
print(s.eatenApples([0, 19], [0, 5]))
print(s.eatenApples([3, 0, 0, 0, 0, 2], [3, 0, 0, 0, 0, 2]))
print(s.eatenApples([1, 2, 3, 5, 2], [3, 2, 1, 4, 2]))
