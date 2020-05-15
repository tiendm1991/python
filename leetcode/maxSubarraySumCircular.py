class Solution:
    def maxSubarraySumCircular(self, a) -> int:
        _max, _maxGlobal = a[0], a[0]
        n = len(a)
        for i in range(1, n):
            _max = max(_max + a[i], a[i])
            _maxGlobal = max(_maxGlobal, _max)
        prefix, suffix = [0] * n, [0] * n
        prefix[0] = a[0]
        suffix[-1] = a[-1]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + a[i]
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] + a[i]
        for i in range(1, n):
            prefix[i] = max(prefix[i], prefix[i - 1])
        for i in range(n - 2, -1, -1):
            suffix[i] = max(suffix[i], suffix[i + 1])
        for i in range(n - 1):
            _maxGlobal = max(_maxGlobal, prefix[i] + suffix[i + 1])
        return _maxGlobal


s = Solution()
print(s.maxSubarraySumCircular([5,-3,5]))
print(s.maxSubarraySumCircular([3,-1,2,-1]))
print(s.maxSubarraySumCircular([-2,-3,-1]))
