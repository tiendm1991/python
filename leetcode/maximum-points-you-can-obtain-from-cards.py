import collections


class Solution:
    def maxScore(self, cardPoints, k: int) -> int:
        n = len(cardPoints)
        prefix, suffix = [0] * (n + 1), [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + cardPoints[i - 1]
            suffix[i] = suffix[i - 1] + cardPoints[n - i]
        _max = 0
        for i in range(k + 1):
            _max = max(_max, prefix[i] + suffix[k - i])
        return _max


s = Solution()
print(s.maxScore([1, 2, 3, 4, 5, 6, 1], 3))
