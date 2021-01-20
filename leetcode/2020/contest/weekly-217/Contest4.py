import heapq


class Solution:
    def minimumDeviation(self, nums) -> int:
        a = []
        for i, x in enumerate(nums):
            if x & 1:
                a.append((x, x * 2))
            else:
                a.append([x])
                while not x & 1:
                    x >>= 1
                a[-1] = (x, a[-1][0])
        heapq.heapify(a)
        lowest = min([x[0] for x in a])
        highest = max([x[0] for x in a])
        res = highest - lowest
        while a:
            cur, maxValue = heapq.heappop(a)
            if cur == maxValue:
                break
            heapq.heappush(a, (cur * 2, maxValue))
            highest = max(highest, cur * 2)
            lowest = a[0][0]
            res = min(res, highest - lowest)
        return res


s = Solution()
print(s.minimumDeviation([3, 5, 7]))
# print(s.minimumDeviation([1, 2, 3, 4]))
# print(s.minimumDeviation([4, 1, 5, 20, 3]))
# print(s.minimumDeviation([2, 10, 8]))
