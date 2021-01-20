# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from leetcode.Util import TreeNode

from leetcode import Util


class Solution:
    idx = 0

    def flipMatchVoyage(self, root: TreeNode, voyage):
        self.idx = 0
        res = []

        def helper(node: TreeNode):
            if node is None:
                return None
            if node.val != voyage[self.idx]:
                return [-1]
            self.idx += 1
            if self.idx == len(voyage):
                return None
            if node.left and node.left.val == voyage[self.idx]:
                left = helper(node.left)
                right = helper(node.right)
                if left == [-1] or right == [-1]:
                    return [-1]
            elif node.right and node.right.val == voyage[self.idx]:
                if node.left:
                    res.append(node.val)
                right = helper(node.right)
                left = helper(node.left)
                if left == [-1] or right == [-1]:
                    return [-1]
            elif node.left or node.right:
                return [-1]
            return None

        h = helper(root)
        return res if h is None else [-1]


s = Solution()
print(s.flipMatchVoyage(Util.createTree([1, 2, None, 3]), [1, 3, 2]))
print(s.flipMatchVoyage(Util.createTree([1, None, 2]), [1, 2]))
print(s.flipMatchVoyage(Util.createTree([1, 2]), [2, 1]))
print(s.flipMatchVoyage(Util.createTree([1, 2, 3]), [1, 3, 2]))
print(s.flipMatchVoyage(Util.createTree([1, 2, 3]), [1, 2, 3]))
