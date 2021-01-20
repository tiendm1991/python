import collections


class Solution:
    def numFriendRequests(self, ages) -> int:
        d = collections.Counter(ages)
        ans = 0
        for a in d:
            for b in d:
                if 0.5 * a + 7 < b:
                    if b == a:
                        ans += d[a] * (d[a] - 1)
                    elif b < a:
                        ans += d[b] * d[a]
        return ans


s = Solution()
print(s.numFriendRequests([16, 16]))
print(s.numFriendRequests([16, 17, 18]))
