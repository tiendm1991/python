import math

from scipy.special import comb
class Solution:
    count = 0
    def getProbability(self, balls) -> float:
        k = len(balls)
        sm = sum(balls)
        n = sm // 2
        numbers_of_space = comb(sm, n)
        maxColor = max(balls)
        combine = [[1 if i == 0 else 0 for i in range(maxColor+1)] for j in range(maxColor+1)]
        for i in range(1, maxColor+1):
            for j in range(1, i+1):
                combine[i][j] = combine[i-1][j] + combine[i-1][j-1]
        def cacule(box1):
            if sum(box1) != n:
                return 0
            k1 = len([1 for x in box1 if x > 0])
            k2 = len([1 for i in range(k) if balls[i] - box1[i] > 0])
            if k1 != k2:
                return 0
            result = 1
            for i in range(k):
                result *= combine[balls[i]][box1[i]]
            return result
        def backtrack(box1, i):
            if len(box1) == k:
                self.count += cacule(box1)
                return
            for j in range(balls[i] + 1):
                if sum(box1) > n:
                    break
                backtrack(box1 + [j], i + 1)
        box1 = [];
        backtrack(box1, 0)
        return self.count / numbers_of_space
s = Solution()
print(s.getProbability([6,6,6,6,6,6]))
