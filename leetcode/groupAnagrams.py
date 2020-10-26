from datetime import datetime
import collections


class Solution:
    def groupAnagrams(self, strs):
        n = len(strs)
        if n == 0:
            return []
        d = {}
        for s in strs:
            sSort = sorted(s) + ['#']
            key = ''
            count = 1
            for i in range(1, len(sSort)):
                if sSort[i] != sSort[i - 1]:
                    key += sSort[i - 1] + str(count)
                    count = 1
                else:
                    count += 1
            if key not in d:
                d[key] = [s]
            else:
                d[key].append(s)
        return list(d.values())


s = Solution()
startTime = datetime.now()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(datetime.now() - startTime)
