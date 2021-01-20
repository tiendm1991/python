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

    def distributeCoins(self, root: TreeNode) -> int:
        self.res = 0

        def helper(node: TreeNode):
            if node is None:
                return 0, 0
            node_left, coin_left = helper(node.left)
            node_right, coin_right = helper(node.right)
            self.res += abs(coin_left - node_left) + abs(coin_right - node_right)
            return node_left + node_right + 1, coin_left + coin_right + node.val

        helper(root)
        return self.res


s = Solution()
print(s.distributeCoins(Util.createTree([0, 3, 0])))
print(s.distributeCoins(Util.createTree([1, 0, 2])))
print(s.distributeCoins(Util.createTree([1, 0, 0, None, 3])))
