import heapq


class Solution:
    def furthestBuilding(self, heights, bricks: int, ladders: int) -> int:
        h = []
        n = len(heights)
        for i in range(n - 1):
            d = heights[i + 1] - heights[i]
            if d <= 0:
                continue
            heapq.heappush(h, d)
            if len(h) > ladders:
                x = heapq.heappop(h)
                if bricks < x:
                    return i
                bricks -= x
        return n - 1


s = Solution()
print(s.furthestBuilding([4, 2, 7, 6, 9, 14, 12], 5, 1))
