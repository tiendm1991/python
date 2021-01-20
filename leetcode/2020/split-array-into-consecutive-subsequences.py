import collections


class Solution:
    def isPossible(self, nums) -> bool:
        d = collections.Counter(nums)
        e = collections.Counter()
        for x in nums:
            if d[x] == 0:
                continue
            d[x] -= 1
            if e[x - 1] > 0:
                e[x] += 1
                e[x - 1] -= 1
            elif d[x + 1] > 0 and d[x + 2] > 0:
                d[x + 1] -= 1
                d[x + 2] -= 1
                e[x + 2] += 1
            else:
                return False
        return True


s = Solution()
print(s.isPossible([1, 2, 3, 3, 4, 5]))
print(s.isPossible([1, 2, 3, 3, 4, 4, 5]))
