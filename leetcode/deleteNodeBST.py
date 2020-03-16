import functools
from datetime import datetime, time
import math
import bisect
import random
import collections

from testcases.cebu import Util
from testcases.cebu.Util import ListNode, TreeNode


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        pre, delNode, isLeft = None, root, True
        while delNode and delNode.val != key:
            pre = delNode
            if delNode.val > key:
                delNode = delNode.left
                isLeft = True
            else:
                delNode = delNode.right
                isLeft = False
        if delNode == None:
            return root
        if delNode.left == None and delNode.right == None:
            if pre == None:
                return None
            if isLeft:
                pre.left = None
            else:
                pre.right = None
        elif delNode.left == None:
            if pre == None:
                return delNode.right
            if isLeft:
                pre.left = delNode.right
            else:
                pre.right = delNode.right
            delNode.right = None
        elif delNode.right == None:
            if pre == None:
                return delNode.left
            if isLeft:
                pre.left = delNode.left
            else:
                pre.right = delNode.left
            delNode.left = None
        else:
            preReplace, replace = None, delNode.right
            while replace.left != None:
                preReplace = replace
                replace = replace.left
            delNode.val = replace.val
            if preReplace:
                preReplace.left = replace.right
            else:
                delNode.right = replace.right
        return root

s = Solution()
startTime = datetime.now()
print(s.deleteNode(Util.createTree([3,1,4,None,2]), 1))
print(datetime.now() - startTime)

