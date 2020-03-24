from datetime import datetime, time
import heapq
import math
import random
import collections

class Solution:
    _min = 2147483647
    _pre = None
    def getMinimumDifference(self, root: TreeNode) -> int:
        def traversal(node: TreeNode, arr):
            if node == None:
                return
            traversal(node.left, arr)
            arr.append(node.val)
            traversal(node.right, arr)
        arr = []
        traversal(root, arr)
        minAbs = arr[-1]
        for i in range(1, len(arr)):
            minAbs = min(minAbs, arr[i] - arr[i-1])
        return minAbs

    def getMinimumDifference2(self, root: TreeNode) -> int:
        def traversal(node: TreeNode):
            if node == None:
                return self._min
            traversal(node.left)
            if self._pre != None:
                self._min = min(self._min, node.val - self._pre)
            self._pre = node.val
            traversal(node.right)
        traversal(root)
        return self._min
s = Solution()
startTime = datetime.now()
print(s.getMinimumDifference2(Util.createTree([6, 3, 9, 1, 5, 7, 12])))
print(datetime.now() - startTime)

