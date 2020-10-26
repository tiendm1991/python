import functools
from datetime import datetime, time
import math
import bisect
import random


class Solution:
    def palindromePairs(self, words):
        n = len(words)
        result = []
        if n < 2:
            return result

        def findPrefixCandidate(s):
            ls = []
            r = s[::-1]
            i = len(r)
            while i > 0:
                x = r[:i]
                combine = x + s
                if combine == combine[::-1]:
                    ls.append(x)
                i -= 1
            if s == r:
                ls.append('')
            return ls

        def findSuffixCandidate(s):
            ls = []
            r = s[::-1]
            n = len(s)
            i = 0
            while i < n:
                x = r[i:]
                combine = s + x
                if combine == combine[::-1]:
                    ls.append(x)
                i += 1
            if s == r:
                ls.append('')
            return ls

        map = {}
        for i in range(n):
            s = words[i]
            r = s[::-1]
            if s in map:
                map[s].add(i)
            else:
                map[s] = {i}

        for i in range(n):
            s = words[i]
            candidatePrefix = findPrefixCandidate(s)
            for c in candidatePrefix:
                if c in map:
                    for j in map[c]:
                        if j != i and [j, i] not in result:
                            result.append([j, i])
            candidateSuffix = findSuffixCandidate(s)
            for c in candidateSuffix:
                if c in map:
                    for j in map[c]:
                        if j != i and [i, j] not in result:
                            result.append([i, j])
        return result


s = Solution()
startTime = datetime.now()
print(s.palindromePairs(["a", "abc", "aba", ""]))
print(datetime.now() - startTime)
