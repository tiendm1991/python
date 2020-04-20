from  datetime import datetime
import functools

from leetcode.Util import TreeNode


class Solution:
    def bstFromPreorder(self, preorder) -> TreeNode:
        def buildTree(a, left, right):
            if left > right:
                return None
            parent = TreeNode(a[left])
            endLeft = left+1
            while endLeft <= right and a[endLeft] < a[left]:
                endLeft += 1
            parent.left = buildTree(a, left+1, endLeft-1)
            parent.right = buildTree(a, endLeft, right)
            return parent
        return buildTree(preorder, 0, len(preorder) - 1)

s = Solution()
startTime = datetime.now()
print(s.bstFromPreorder([8,5,1,7,10,12]))
print(datetime.now() - startTime)