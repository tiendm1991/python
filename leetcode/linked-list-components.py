# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from leetcode.Util import ListNode
from leetcode import Util


class Solution:
    def numComponents(self, head: ListNode, g) -> int:
        cur = head
        while cur.val not in g:
            cur = cur.next
        ans = 1
        pre = cur
        cur = cur.next
        while cur:
            if cur.val in g and pre.val not in g:
                ans += 1
            pre = cur
            cur = cur.next
        return ans


s = Solution()
print(s.numComponents(Util.createListNode([0, 1, 2, 3, 4]), {0, 3, 1, 4}))
