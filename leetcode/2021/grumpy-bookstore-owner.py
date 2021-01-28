class Solution:
    def maxSatisfied(self, customers, grumpy, X: int) -> int:
        n = len(customers)
        s = sum([customers[i] * (1 - grumpy[i]) for i in range(n)])
        add = 0
        maxAdd = 0
        for i in range(n):
            if grumpy[i] == 1:
                add += customers[i]
            if i >= X and grumpy[i - X] == 1:
                add -= customers[i - X]
            maxAdd = max(maxAdd, add)
        return s + maxAdd


s = Solution()
print(s.maxSatisfied([2, 6, 6, 9],
                     [0, 0, 1, 1], 1))
print(s.maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5],
                     [0, 1, 0, 1, 0, 1, 0, 1], 3))
print(s.maxSatisfied([10, 1, 7],
                     [0, 0, 0], 2))
