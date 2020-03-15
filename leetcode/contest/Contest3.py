import queue


class Solution:
    def maxPerformance(self, n: int, speed, efficiency, k) -> int:
        mod = 10**9+7
        s = sum(speed)
        dp = sorted([[efficiency[i], speed[i]] for i in range(n)], key=lambda x: x[0])
        idx = 0
        while idx < n - 1:
            sTmp = s - dp[idx][1]
            j = idx + 1
            while j < n - 1 and dp[j][0] == dp[idx][0]:
                sTmp -= dp[j][1]
                j += 1
            if sTmp * dp[j][0] <= s * dp[idx][0]:
                break
            s = sTmp
            idx = j
        dp = dp[idx:]
        result = s * dp[0][0]
        while len(dp) > 1:
            _max, _maxIdx = (s - dp[0][1]) * dp[1][0], 0
            for i in range(1, len(dp)):
                tmp = (s - dp[i][1]) * dp[0][0]
                if tmp > _max:
                    _max, _maxIdx = tmp, i
            s -= dp[_maxIdx][1]
            del dp[_maxIdx]
            if len(dp) > k:
                result = None
                continue
            elif len(dp) == k:
                result = _max
            else:
                result = max(result, _max)
        return result % (mod)
s = Solution()
print(s.maxPerformance(3,
[4,6,8],
[4,5,10],
3))