from datetime import datetime
class Solution:
    def stoneGameIII(self, stoneValue) -> str:
        n = len(stoneValue)
        if n == 0:
            return 'Tie'
        dp = [0] * n
        s = 0
        for i in range(n-1, -1, -1):
            s += stoneValue[i]
            if i == n-1:
                dp[i] = s
            elif i == n-2:
                dp[i] = max(stoneValue[i], s)
            elif i == n-3:
                dp[i] = max(stoneValue[i] + s - dp[i+1], stoneValue[i] + stoneValue[i+1], s)
            else:
                dp[i] = max(s - dp[i+1], s- dp[i+2], s - dp[i+3])
        return 'Alice' if dp[0] > s - dp[0] else 'Bob' if dp[0] < s - dp[0] else 'Tie'

    def stoneGameIII2(self, stoneValue) -> str:
        n = len(stoneValue)
        if n == 0:
            return 'Tie'
        n += 3
        dp = [0] * n
        s = 0
        for i in range(n - 4, -1, -1):
            s += stoneValue[i]
            dp[i] = max(s - dp[i + 1], s - dp[i + 2], s - dp[i + 3])
        return 'Alice' if dp[0] > s - dp[0] else 'Bob' if dp[0] < s - dp[0] else 'Tie'

pattern = Solution()
startTime = datetime.now()
print(pattern.stoneGameIII([-1,-2,-3]))
print(pattern.stoneGameIII2([-1,-2,-3]))
print(datetime.now() - startTime)