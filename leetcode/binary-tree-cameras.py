# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from leetcode.Util import TreeNode

from leetcode import Util


class Solution:
    res = 0

    def minCameraCover(self, root: TreeNode) -> int:
        self.res = 0
        NOT_MONITOR = 0
        MONITOR_OTHER = 1
        PUT_CAMERA = 2

        def helper(node: TreeNode, par: TreeNode):
            if node is None:
                return None
            left = helper(node.left, node)
            right = helper(node.right, node)
            if left == NOT_MONITOR or right == NOT_MONITOR:
                self.res += 1
                return PUT_CAMERA
            if left == PUT_CAMERA or right == PUT_CAMERA:
                return MONITOR_OTHER
            if par is None:
                self.res += 1
                return PUT_CAMERA
            return NOT_MONITOR

        helper(root, None)
        return self.res


s = Solution()
print(s.minCameraCover(Util.createTree([0, 0, 0, None, None, None, 0])))
print(s.minCameraCover(Util.createTree([0, None, 0, None, 0, None, 0])))
print(s.minCameraCover(Util.createTree([0, 0, None, 0, None, 0, None, None, 0])))
print(s.minCameraCover(Util.createTree([0, 0, None, 0, 0])))
print(s.minCameraCover(Util.createTree([0, 0, 0, None, None, None, 0, None, 0])))
print(s.minCameraCover(Util.createTree([0, 0, 0, None, None, None, 0])))
print(s.minCameraCover(Util.createTree([0, 0, None, 0, None, 0, None, None, 0])))
print(s.minCameraCover(Util.createTree([0])))
