# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from leetcode.Util import ListNode

from leetcode import Util


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        i = 0
        cur = list1
        while i < a - 1:
            cur = cur.next
            i += 1
        cur2 = cur
        while i <= b:
            cur2 = cur2.next
            i += 1
        cur.next = list2
        cur3 = list2
        while cur3.next:
            cur3 = cur3.next
        cur3.next = cur2
        return list1


s = Solution()
print(s.mergeInBetween(Util.createListNode([0, 1, 2, 3, 4, 5]), 3, 3, Util.createListNode([100, 101, 102])))
