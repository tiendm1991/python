from datetime import datetime
import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = collections.Counter(s1)
        n1, n2 = len(s1), len(s2)
        if n2 < n1:
            return False
        d2 = {}
        start = 0
        for i in range(len(s2)):
            ch = s2[i]
            if ch not in d1:
                d2 = {}
                start = i + 1
            else:
                d2[ch] = d2.get(ch, 0) + 1
                if i - start + 1 == n1:
                    if d1 == d2:
                        return True
                    else:
                        d2[s2[start]] -= 1
                        start += 1
        return False


s = Solution()
startTime = datetime.now()
print(s.checkInclusion('abac', 'eidbaaaabcooo'))
print(datetime.now() - startTime)
