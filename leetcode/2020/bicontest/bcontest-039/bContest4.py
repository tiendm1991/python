import collections
import bisect


class Solution:
    def canDistribute(self, nums, quantity) -> bool:
        a = collections.Counter(nums)
        q = sorted(quantity, reverse=True)
        n, m = len(a), len(q)
        a = sorted(a.values())[-m:]

        def backtrack(idx):
            if idx == m:
                return True
            for i in range(len(a)):
                if a[i] >= q[idx]:
                    a[i] -= q[idx]
                    if backtrack(idx + 1):
                        return True
                    a[i] += q[idx]
            return False

        return backtrack(0)


s = Solution()
print(s.canDistribute([154, 533, 533, 533, 154, 154, 533, 154, 154], [3, 2, 2, 2]))
# print(s.canDistribute([1, 2, 3, 3], [2]))
# print(s.canDistribute([1, 1, 2, 2], [2, 2]))
