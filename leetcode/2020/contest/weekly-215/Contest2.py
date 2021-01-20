import collections


class Solution:
    def closeStrings(self, w1: str, w2: str) -> bool:
        if len(w1) != len(w2):
            return False
        d1 = collections.Counter(w1)
        d2 = collections.Counter(w2)
        a1 = sorted(d1.values())
        a2 = sorted(d2.values())
        b1 = sorted(d1.keys())
        b2 = sorted(d2.keys())
        return a1 == a2 and b1 == b2


s = Solution()
print(s.closeStrings("uau", "ssx"))
print(s.closeStrings("cabbba", "abbccc"))
# acbbbc
