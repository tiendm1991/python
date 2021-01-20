import heapq


class Solution:
    def mincostToHireWorkers(self, quality, wage, K: int) -> float:
        infos = sorted([[w / q, q] for w, q in zip(wage, quality)])
        h = []
        ans = 10 ** 9
        qsum = 0
        for r, q in infos:
            heapq.heappush(h, -q)
            qsum += q
            if len(h) > K:
                qsum += heapq.heappop(h)
            if len(h) == K:
                ans = min(ans, qsum * r)
        return ans


s = Solution()
print(s.mincostToHireWorkers([25, 20, 19], [70, 50, 30], 2))
