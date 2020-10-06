import collections


class Solution:
    def numRabbits(self, answers) -> int:
        d = collections.Counter(answers)
        ans = 0
        for k in d:
            # c1: ans += d[k] + (k + 1) - ((d[k] - 1) % (k + 1) + 1)
            # c2: ans += d[k] + k - (d[k] - 1) % (k + 1)
            ans += ((d[k] - 1) // (k + 1) + 1) * (k + 1)
        return ans


s = Solution()
print(s.numRabbits([1, 0, 1, 0, 0]))
