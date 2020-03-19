from datetime import datetime, time
import heapq
import math

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode):
        d = {}
        def find(node: TreeNode):
            if node == None:
                return 0
            left = find(node.left)
            right = find(node.right)
            s = left + right + node.val
            d[s] = d.get(s, 0) + 1
            return s
        find(root)
        result, _max = [], 0
        for k in d:
            if d[k] > _max:
                result = [k]
                _max = d[k]
            elif d[k] == _max:
                result.append(k)
        return result


s = Solution()
startTime = datetime.now()
print(s.findFrequentTreeSum(Util.createTree([5,2, -5])))
print(datetime.now() - startTime)

