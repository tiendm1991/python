# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from leetcode.Util import TreeNode

from leetcode import Util


class Solution:
    def flipEquiv(self, root1: TreeNocherryPickupde, root2: TreeNode) -> bool:
        def canFlip(node1: TreeNode, node2: TreeNode):
            if node1 is None:
                return node2 is None
            if node2 is None:
                return node1 is None
            if node1.val != node2.val:
                return False
            return (canFlip(node1.left, node2.left) and canFlip(node1.right, node2.right)) or \
                   (canFlip(node1.left, node2.right) and canFlip(node1.right, node2.left))

        return canFlip(root1, root2)


s = Solution()
print(s.flipEquiv(Util.createTree([1, 2, 3, 4, 5, 6, None, None, None, 7, 8]),
                  Util.createTree([1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7])))
