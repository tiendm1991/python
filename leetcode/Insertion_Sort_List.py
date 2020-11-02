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
        last = headTmp
        while cur is not None:
            tmp = cur.next
            insertPos = headTmp.next
            preInsert = headTmp
            while insertPos.val < cur.val:
                preInsert = insertPos
                insertPos = insertPos.next
            if insertPos == cur:
                last = cur
            else:
                preInsert.next = cur
                cur.next = insertPos
                last.next = tmp
            cur = tmp
        return headTmp.next


s = Solution()
print(s.insertionSortList(Util.createListNode([3, 2, 4])))
# print(s.insertionSortList(Util.createListNode([4, 2, 1, 3, 1, 2])))
