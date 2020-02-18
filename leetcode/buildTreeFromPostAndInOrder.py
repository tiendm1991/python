# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        def build(_in, _post, inStart, inEnd, postStart):
            if inStart > inEnd:
                return None
            root = TreeNode(_post[postStart])
            idx = _in.index(_post[postStart])
            root.right = build(_in, _post, idx+1, inEnd, postStart - 1)
            root.left = build(_in, _post, inStart, idx-1, postStart - (inEnd - idx + 1))
            return root
        tree = build(inorder, postorder, 0, len(inorder)-1, len(postorder)-1)
        return tree
