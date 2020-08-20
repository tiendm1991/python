# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import Util
from Util import ListNode


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head
        stack = []
        slow, fast = head, head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        while slow != None:
            stack.append(slow)
            slow = slow.next
        cur = head
        while len(stack) > 1:
            tmp = cur.next
            top = stack.pop()
            cur.next = top
            top.next = tmp
            cur = tmp
        top = stack.pop()
        if cur != top:
            cur.next = top
        top.next = None
        return


s = Solution()
print(s.reorderList(Util.createListNode([1, 2, 3, 4, 5])))
