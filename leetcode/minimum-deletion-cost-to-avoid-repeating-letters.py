class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        s += '@'
        n = len(s)
        start, count = 0, 1
        ans = 0
        for i in range(1, n):
            if s[i] == s[start]:
                count += 1
                continue
            else:
                if count > 1:
                    _max = 0
                    for j in range(start, i):
                        ans += cost[j]
                        if cost[j] > _max:
                            _max = cost[j]
                    ans -= _max
                start, count = i, 1
        return ans