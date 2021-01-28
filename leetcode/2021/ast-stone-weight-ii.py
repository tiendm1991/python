class Solution:
    def lastStoneWeightII(self, stones) -> int:
        _set = {0}
        S = sum(stones)
        res = float("inf")
        for i in range(len(stones)):
            newSet = set()
            for pre in _set:
                x = stones[i] + pre
                res = min(res, abs(2 * x - S))
                newSet.add(x)
            _set = _set.union(newSet)
        return res


s = Solution()
print(s.lastStoneWeightII([1, 2]))
print(s.lastStoneWeightII([2, 7, 4, 1, 8, 1]))
