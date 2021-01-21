# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from leetcode.Util import ListNode

from leetcode import Util


class Solution:
    def nextLargerNodes(self, head: ListNode):
        stack = []
        res = []
        cur, i = head, 0
        while cur:
            while stack and stack[-1][1] < cur.val:
                res[stack.pop()[0]] = cur.val
            stack.append((i, cur.val))
            i += 1
            cur = cur.next
            res.append(0)
        return res


s = Solution()
print(s.nextLargerNodes(Util.createListNode([2, 7, 4, 3, 5])))
print(s.nextLargerNodes(Util.createListNode([1, 7, 5, 1, 9, 2, 5, 1])))
