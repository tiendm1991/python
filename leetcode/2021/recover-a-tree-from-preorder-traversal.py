# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from leetcode.Util import TreeNode

from leetcode import Util


class Solution:
    def recoverFromPreorder(self, s: str) -> TreeNode:
        d = "0123456789"
        s += '-'
        n = len(s)
        i = 0
        j = 0
        stack = []
        while i < n - 1:
            if s[i] in d and s[i + 1] == "-":
                level = 0
                while j < i:
                    if s[j] == '-':
                        j += 1
                        level += 1
                    else:
                        break
                val = int(s[j: i + 1])
                j = i + 1
                if not stack:
                    stack.append((TreeNode(val), level))
                elif level > stack[-1][1]:
                    left = TreeNode(val)
                    stack[-1][0].left = left
                    stack.append((left, level))
                else:
                    while stack[-1][1] >= level:
                        stack.pop()
                    right = TreeNode(val)
                    stack[-1][0].right = right
                    stack.append((right, level))
            i += 1
        return stack[0][0]


s = Solution()
print(s.recoverFromPreorder("1-2--3--4-5--6--7"))
print(s.recoverFromPreorder("1-2--3---4-5--6---7"))
print(s.recoverFromPreorder("1-401--349---90--88"))
