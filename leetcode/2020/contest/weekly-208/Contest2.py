class Solution:
    def minOperationsMaxProfit(self, customers, boardingCost, runningCost) -> int:
        ans = -1
        n = len(customers)
        wait = 0
        cost = 0
        maxP = 0
        i, j = 1, 0
        while j < n or wait > 0:
            if j < n:
                wait += customers[j]
                j += 1
            cost += min(wait, 4) * boardingCost - runningCost
            if cost > maxP:
                ans = i
                maxP = cost
            wait = max(wait - 4, 0)
            i += 1
        return ans


s = Solution()
print(s.minOperationsMaxProfit([10, 10, 6, 4, 7], 3, 8))
