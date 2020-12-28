class Solution:
    def boxDelivering_n2(self, boxes, portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        MAX_INT = 10 ** 9 + 7
        n = len(boxes)
        dp = [MAX_INT] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            j = i
            w = 0
            t = 2
            while j >= max(1, i - maxBoxes + 1) and w + boxes[j - 1][1] <= maxWeight:
                if j < i and boxes[j - 1][0] != boxes[j][0]:
                    t += 1
                dp[i] = min(dp[i], dp[j - 1] + t)
                w += boxes[j - 1][1]
                j -= 1
        return dp[-1]

    def boxDelivering(self, boxes, portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        n = len(boxes)
        need = j = lastj = 0
        dp = [0] + [float('inf')] * n
        b, w = 0, 0
        for i in range(n):
            while j < n and b < maxBoxes and w + boxes[j][1] <= maxWeight:
                b += 1
                w += boxes[j][1]
                if j == 0 or boxes[j][0] != boxes[j - 1][0]:
                    lastj = j
                    need += 1
                j += 1

            dp[j] = min(dp[j], dp[i] + need + 1)
            dp[lastj] = min(dp[lastj], dp[i] + need)

            b -= 1
            w -= boxes[i][1]
            if i == n - 1 or boxes[i][0] != boxes[i + 1][0]:
                need -= 1
        return dp[n]


s = Solution()
print(s.boxDelivering([[1, 4], [1, 2], [2, 1], [2, 1], [3, 2], [3, 4]], 3, 6, 7))
# print(s.boxDelivering([[1, 1], [2, 1], [1, 1]], 2, 3, 3))
# print(s.boxDelivering([[1, 2], [3, 3], [3, 1], [3, 1], [2, 4]], 3, 6, 6))
# print(s.boxDelivering([[2, 4], [2, 5], [3, 1], [3, 2], [3, 7], [3, 1], [4, 4], [1, 3], [5, 2]], 5, 5, 7))
