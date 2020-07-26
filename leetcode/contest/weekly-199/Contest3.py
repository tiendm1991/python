# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from leetcode import Util
from leetcode.Util import TreeNode


class Solution:
    ans = 0

    def countPairs(self, root: TreeNode, distance: int) -> int:
        def recursive(node: TreeNode):
            d = {}
            if node is None:
                return d
            if node.left is None and node.right is None:
                d[node] = 0
                return d
            dl = recursive(node.left)
            dr = recursive(node.right)
            for l in dl:
                d[l] = dl[l] + 1
            for r in dr:
                d[r] = dr[r] + 1
            if dl and dr:
                for l in dl:
                    for r in dr:
                        if d[l] + d[r] <= distance:
                            self.ans += 1
            return d

        recursive(root)
        return self.ans


s = Solution()
print(s.countPairs(Util.createTree([7,1,4,6,None,5,3,None,None,None,None,None,2]), 3))
