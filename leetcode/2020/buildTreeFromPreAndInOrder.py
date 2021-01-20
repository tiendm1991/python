# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    preStart = 0

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None

        def build(_pre, _in, inStart, inEnd):
            if inStart > inEnd:
                return None
            root = TreeNode(_pre[self.preStart])
            idx = _in.index(_pre[self.preStart])
            self.preStart += 1
            root.left = build(_pre, _in, inStart, idx - 1)
            root.right = build(_pre, _in, idx + 1, inEnd)
            return root

        tree = build(preorder, inorder, 0, len(preorder) - 1)
        return tree
