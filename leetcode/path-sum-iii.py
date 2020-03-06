import functools
from datetime import datetime, time
import math
import bisect
import random
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def createTree(arr):
    if arr == None or len(arr) == 0:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while i < len(arr):
        while queue[0] == None:
            del queue[0]
        left, right = None, None
        if arr[i] != None:
            left = TreeNode(arr[i])
        queue[0].left = left
        queue.append(left)
        i += 1
        if i == len(arr):
            break
        if arr[i] != None:
            right = TreeNode(arr[i])
        queue[0].right = right
        queue.append(right)
        i += 1
        del queue[0]
    return root

class Solution:
    count = 0
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def traversal(node: TreeNode, prefixSum):
            if node == None:
                return
            s = node.val
            s += prefixSum[-1]
            self.count += prefixSum.count(s - sum)
            prefixSum.append(s)
            traversal(node.left, prefixSum)
            traversal(node.right, prefixSum)
            prefixSum.pop()
            return
        traversal(root, [0])
        return self.count


s = Solution()
startTime = datetime.now()
print(s.pathSum(createTree([10,5,-3,3,2,None,11,3,-2,None,1]), 8))
print(datetime.now() - startTime)

