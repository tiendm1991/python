# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from leetcode.Util import ListNode

from leetcode import Util


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        headTmp = ListNode(0)
        headTmp.next = head
        cur = head
        i = 1
        while cur and i < k:
            cur = cur.next
            i += 1
        cur2 = cur
        cur1 = headTmp
        while cur:
            cur = cur.next
            cur1 = cur1.next
        cur1.val, cur2.val = cur2.val, cur1.val
        return headTmp.next


s = Solution()
print(s.swapNodes(Util.createListNode([1, 2, 3, 4, 5]), 2))
