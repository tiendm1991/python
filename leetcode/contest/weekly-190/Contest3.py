from leetcode import Util
from leetcode.Util import TreeNode


class Solution:
    count = 0

    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        if root is None:
            return False
        def traversal(node, d):
            if node.left is None and node.right is None:
                if node.val in d:
                    d.remove(node.val)
                else:
                    d.add(node.val)
                self.count += 1 if len(d) <= 1 else 0
                return
            if node.val in d:
                if node.left:
                    traversal(node.left, d - {node.val})
                if node.right:
                    traversal(node.right, d - {node.val})
            else:
                if node.left:
                    traversal(node.left, d | {node.val})
                if node.right:
                    traversal(node.right, d | {node.val})
        traversal(root, set())
        return self.count

s = Solution()
print(s.pseudoPalindromicPaths(Util.createTree([1,9,1,None,1,None,1,None,None,7,None,None,4])))
