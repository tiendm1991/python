# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(root, _min, _max):
            if root == None:
                return True
            if _max != None and root.val >= _max:
                return False
            if _min != None and root.val <= _min:
                return False
            l = valid(root.left, _min, root.val)
            if not l:
                return False
            r = valid(root.right, root.val, _max)
            if not r:
                return False
            return True

        return valid(root, None, None)
