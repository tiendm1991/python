from string import digits


class Solution:
    def maxPerformance(self, n: int, speed, efficiency, k) -> int:
        dp = speed[::]
        selected = [i for i in range(k)]
        dp[k-1] = sum(speed[:k]) * min(efficiency[:k])
        for i in range(k, n):
            s = 0
            for j in selected:
                s += speed[j]
            s += speed[i]
            x = [0] * k
            for j in range(k):
                a = selected[:j] + selected[j+1:] + [i]
                a = [efficiency[_] for _ in a]
                x[j] = min(a) * (s - speed[selected[j]])
            _max = max(x)
            dp[i] = max(dp[i-1], _max)
            if _max > dp[i-1]:
                for j in range(k):
                    if x[j] == _max:
                        selected = selected[:j] + selected[j+1:] + [i]
                        break
        return dp[n-1]
s = Solution()
print(s.maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 2))