# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from leetcode import Util
from leetcode.Util import TreeNode


class Solution:
    parent1, parent2 = None, None
    depth1, depth2 = -1, -1

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        def dfs(node, depth):
            if node is None:
                return
            if node.left:
                if node.left.val == x:
                    self.depth1 = depth
                    self.parent1 = node
                elif node.left.val == y:
                    self.depth2 = depth
                    self.parent2 = node
                else:
                    dfs(node.left, depth + 1)
            if node.right:
                if node.right.val == x:
                    self.depth1 = depth
                    self.parent1 = node
                elif node.right.val == y:
                    self.depth2 = depth
                    self.parent2 = node
                else:
                    dfs(node.right, depth + 1)

        dfs(root, 0)
        if self.parent1 is None or self.parent2 is None or self.depth1 == -1 or self.depth2 == -1:
            return False
        return self.depth1 == self.depth2 and self.parent1 != self.parent2


s = Solution()
print(s.isCousins(Util.createTree([1, None, 2, 3, None, None, 4, None, 5]), 1, 3))
