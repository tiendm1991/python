from leetcode.Util import TreeNode

from leetcode import Util


class Solution:
    ans = 0

    def sumRootToLeaf(self, root: TreeNode) -> int:
        if root is None:
            return 0

        def help(node):
            if node is None:
                return []
            if node.left is None and node.right is None:
                self.ans += node.val
                return [1]
            left, right = help(node.left), help(node.right)
            result = []
            for x in left:
                self.ans += node.val * 2 ** x
                result.append(x + 1)
            for x in right:
                self.ans += node.val * 2 ** x
                result.append(x + 1)
            return result

        help(root)
        return self.ans


s = Solution()
print(s.sumRootToLeaf(Util.createTree([1,1])))
