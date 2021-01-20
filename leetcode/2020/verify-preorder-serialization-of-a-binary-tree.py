import functools
from datetime import datetime, time
import math


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        order = preorder.split(',')
        n = len(order)

        def valid(s):
            if s[0] == '#':
                return len(s) == 1
            newS = [s[0]]
            for i in range(1, len(s)):
                if s[i] != '#' or newS[i - 1] != '#':
                    newS.append(s[i])
                else:
                    newS.pop()
                    newS[-1] = '#'
                    if i < len(s):
                        newS += s[i + 1:]
                    return valid(newS)
            return False

        return valid(order)


s = Solution()
startTime = datetime.now()
print(s.isValidSerialization("1, #"))
print(datetime.now() - startTime)
