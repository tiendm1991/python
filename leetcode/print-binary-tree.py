# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from leetcode.Util import TreeNode
from leetcode import Util


class Solution:
    def printTree(self, root: TreeNode):
        def get_height(node: TreeNode):
            if node is None:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))

        h = get_height(root)
        w = 2 ** h - 1
        ans = [["" for j in range(w)] for i in range(h)]
        d = 0
        q = [root]
        idx = [[0, w - 1]]
        while d < h:
            newQ = []
            newIdx = []
            for i, node in enumerate(q):
                pos = idx[i]
                m = (pos[0] + pos[1]) // 2
                newIdx.append([pos[0], m - 1])
                newIdx.append([m + 1, pos[1]])
                if node is None:
                    newQ += [None, None]
                else:
                    ans[d][(pos[0] + pos[1]) // 2] = str(node.val)
                    newQ.append(node.left)
                    newQ.append(node.right)
            q = newQ
            idx = newIdx
            d += 1
        return ans


s = Solution()
print(s.printTree(Util.createTree([1, 2, 3, None, 4])))
