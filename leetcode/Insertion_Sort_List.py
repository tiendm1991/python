# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from leetcode.Util import ListNode
from leetcode import Util


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        headTmp = ListNode(-10 ** 9)
        headTmp.next = head
        cur = head
        pre = headTmp
        while cur is not None:
            tmp = cur.next
            cur2 = head
            pre2 = headTmp
            while cur2.val < cur.val:
                pre2 = cur2
                cur2 = cur2.next
            if cur2.val == cur.val:
                pre = cur
                cur = tmp
            else:
                pre2.next = cur
                cur.next = cur2
                pre.next = tmp
                cur = tmp
        return headTmp.next


s = Solution()
print(s.insertionSortList(Util.createListNode([4, 2, 1, 3])))
