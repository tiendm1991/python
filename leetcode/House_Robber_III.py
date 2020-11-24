# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from leetcode.Util import TreeNode

from leetcode import Util


class Solution:
    def rob1(self, root: TreeNode) -> int:
        dp = {}

        def helper(node):
            if node is None:
                return 0
            if node in dp:
                return dp[node]
            x1, x2, x3, x4 = 0, 0, 0, 0
            if node.left:
                x1, x2 = helper(node.left.left), helper(node.left.right)
            if node.right:
                x3, x4 = helper(node.right.left), helper(node.right.right)
            dp[node] = max(helper(node.left) + helper(node.right), x1 + x2 + x3 + x4 + node.val)
            return dp[node]

        return helper(root)

    def rob(self, root: TreeNode) -> int:
        def helper(node):
            if node is None:
                return [0, 0]
            left = helper(node.left)
            right = helper(node.right)
            return [node.val + left[1] + right[1], max(left[0], left[1]) + max(right[0], right[1])]

        return max(helper(root))


s = Solution()
print(s.rob(Util.createTree([3, 2, 6, None, 3, None, 1])))
