class Solution:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0
        s = 0
        smallestIdx = 0
        prices.append(prices[-1] - 1)
        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]:
                s += prices[i-1] - prices[smallestIdx]
                smallestIdx = i
        return s

s = Solution()
print(s.maxProfit([1,6,5,4,2,3,4,5]))
