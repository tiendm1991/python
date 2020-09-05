from leetcode.Util import TreeNode

from leetcode import Util


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode):
        st1, st2, result = [root1] if root1 else [], [root2] if root2 else [], []
        while st1 or st2:
            n1, n2 = st1[-1] if st1 else None, st2[-1] if st2 else None
            if n1 and n1.left:
                st1.append(n1.left)
                n1.left = None
                continue
            if n2 and n2.left:
                st2.append(n2.left)
                n2.left = None
                continue
            if n1 and (not n2 or n1.val <= n2.val):
                result.append(n1.val)
                st1.pop()
                if n1.right:
                    st1.append(n1.right)
                    continue
            else:
                result.append(n2.val)
                st2.pop()
                if n2.right:
                    st2.append(n2.right)
                    continue
        return result


s = Solution()
# print(s.getAllElements(Util.createTree([2, 1, 4]), Util.createTree([1, 0, 3])))
print(s.getAllElements(Util.createTree([]), Util.createTree([5, 1, 7, 0, 2])))
