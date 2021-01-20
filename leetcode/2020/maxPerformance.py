from datetime import datetime, time
import heapq


class HeapElement:
    def __init__(self, val: int):
        self.val = val

    def __cmp__(self, other):
        return self.val[1] - other.val[1]

    def __lt__(self, other):
        return self.val[1] < other.val[1]


class Solution:
    def maxPerformance(self, n: int, speed, efficiency, k) -> int:
        mod = 10 ** 9 + 7
        dp = sorted([[efficiency[i], speed[i]] for i in range(n)], key=lambda x: x[0], reverse=True)
        s = dp[0][1]
        _max = s * dp[0][0]
        cur = [HeapElement(dp[0])]
        for i in range(1, n):
            s += dp[i][1]
            if len(cur) > k - 1:
                remove = heapq.heappop(cur).val
                s -= remove[1]
            _max = max(_max, dp[i][0] * s)
            heapq.heappush(cur, HeapElement(dp[i]))
        return _max % mod


s = Solution()
startTime = datetime.now()
print(s.maxPerformance(6,
                       [2, 10, 3, 1, 5, 8],
                       [5, 4, 3, 9, 7, 2],
                       4))
print(datetime.now() - startTime)
