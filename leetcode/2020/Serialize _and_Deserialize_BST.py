from leetcode.Util import TreeNode

from leetcode import Util


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """

        def help(node: TreeNode):
            if node is None:
                return ""
            s = [str(node.val)]
            s += help(node.left)
            s += help(node.right)
            return s

        return '|'.join(help(root))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if data == "":
            return None
        a = [int(x) for x in data.split("|")]

        def help(left, right):
            if left > right:
                return None
            node = TreeNode(a[left])
            i = left + 1
            while i <= right and a[i] < a[left]:
                i += 1
            node.left = help(left + 1, i - 1)
            node.right = help(i, right)
            return node

        return help(0, len(a) - 1)


# Your Codec object will be instantiated and called as such:
c = Codec()
root = Util.createTree([41, 37, 44, 24, 39, 42, 48, 1, 35, 38, 40])
s = c.serialize(root)
print(s)
r = c.deserialize(s)
print(r)
