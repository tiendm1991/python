import collections


class Solution:
    def customSortString(self, S: str, T: str) -> str:
        d = collections.Counter(T)
        ans = ""
        for c in S:
            if c in d:
                ans += c * d[c]
                del d[c]
        for c in d:
            ans += c * d[c]
        return ans


s = Solution()
print(s.customSortString("kqep", "pekeq"))
