from leetcode.Util import TreeNode

from leetcode import Util


class Solution:
    ans = None
    deepest = -1

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def helper(node: TreeNode):
            if node is None:
                return None, 0
            left = helper(node.left)
            right = helper(node.right)
            if (left[0] is None and right[0] is None) or (left[1] == right[1]):
                return node, left[1] + 1
            elif left[1] > right[1]:
                return left[0], left[1] + 1
            else:
                return right[0], right[1] + 1

        return helper(root)[0]


s = Solution()
print(s.subtreeWithAllDeepest(Util.createTree([0, 2, 1, None, None, 3])))
print(s.subtreeWithAllDeepest(Util.createTree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])))
