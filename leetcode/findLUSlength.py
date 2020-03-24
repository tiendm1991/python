from datetime import datetime, time
import heapq
import math

import random
import collections
class Solution:
    def findLUSlength(self, strs) -> int:
        _max = -1
        d = collections.Counter(strs)
        duplicate = [s for s in d if d[s] > 1]
        candidate = [s for s in d if d[s] == 1]
        if len(candidate) == 0:
            return -1
        def isSubsequnce(s1, s2):
            if len(s1) > len(s2):
                return False
            i, j = 0, 0
            while j < len(s1):
                if i == len(s2):
                    return False
                if s2[i] == s1[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            return True
        for s in candidate:
            check = True
            for s2 in duplicate:
                if isSubsequnce(s, s2):
                    check = False
                    break
            if check:
                _max = max(_max, len(s))
        return _max
s = Solution()
startTime = datetime.now()
print(s.findLUSlength(["aabbcc", "aabbcc","bc","bcc","aabbccc"]))
print(datetime.now() - startTime)

