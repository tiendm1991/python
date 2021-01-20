from leetcode import Util
from leetcode.Util import TreeNode


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        q = [root]
        _max = 1
        while q:
            nextQ = []
            start, end, i = -1, -1, 0
            for node in q:
                if type(node) is int:
                    nextQ.append(2 * node)
                    i += 2 * node
                else:
                    if node.left:
                        end = i
                        if start == -1:
                            start = i
                        nextQ.append(node.left)
                    else:
                        if nextQ and type(nextQ[-1]) is int:
                            nextQ[-1] += 1
                        else:
                            nextQ.append(1)
                    if node.right:
                        end = i + 1
                        if start == -1:
                            start = i + 1
                        nextQ.append(node.right)
                    else:
                        if nextQ and type(nextQ[-1]) is int:
                            nextQ[-1] += 1
                        else:
                            nextQ.append(1)
                    i += 2
            if end != -1:
                _max = max(_max, end - start + 1)
                q = nextQ
            else:
                q = []
        return _max


s = Solution()
print(s.widthOfBinaryTree(
    Util.createTree([-64, 12, 18, -4, -53, None, 76, None, 78, None, -31, 27, 60, 74, None, None, 8, None, 98])))
