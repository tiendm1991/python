# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from leetcode.Util import TreeNode

from leetcode import Util
import functools


class Solution:
    def verticalTraversal(self, root: TreeNode):
        res = []
        d = {}

        def compare(a1, a2):
            if a1[0] != a2[0]:
                return a2[0] - a1[0]
            else:
                return a1[1] - a2[1]

        def traversal(node: TreeNode, x, y):
            if node is None:
                return
            if x not in d:
                d[x] = [[y, node.val]]
            else:
                d[x].append([y, node.val])
            traversal(node.left, x - 1, y - 1)
            traversal(node.right, x + 1, y - 1)

        traversal(root, 0, 0)
        for k, v in sorted(d.items()):
            res.append([a[1] for a in sorted(v, key=functools.cmp_to_key(compare))])

        return res


s = Solution()
print(s.verticalTraversal(Util.createTree([3, 9, 20, None, None, 15, 7])))
