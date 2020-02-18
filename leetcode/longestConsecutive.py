from datetime import datetime, time

#from testcases.cebu.Util import *

class Solution:
    def longestConsecutive(self, nums) -> int:
        _parent = {}
        _exist = {}
        def find(parent, x):
            while parent[x] != x:
                x = parent[x]
            return x
        def updateChild(parent, x, newParent):
            _max = x
            for key in parent:
                if parent[key] == x and key > _max:
                    _max = key
            parent[_max] = newParent
        for x in nums:
            if x in _exist:
                continue
            _parent[x] = x
            if x-1 in _exist:
                newParent = find(_parent, x-1)
                updateChild(_parent, x, newParent)
            if x + 1 in _exist:
                newParent = find(_parent, x)
                updateChild(_parent, x+1, newParent)
            _exist[x] = 1
        _max = 0
        if len(_parent) == 0:
            return 0
        for key in _parent:
            _max = max(_max, key - _parent[key]+1)
        return _max

s = Solution()
start = datetime.now()
print(s.longestConsecutive([1,-8,7,-2,-4,-4,6,3,-4,0,-7,-1,5,1,-9,-3]))
print(datetime.now() - start)

