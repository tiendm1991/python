# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from leetcode.Util import ListNode
from leetcode import Util
import heapq


class Solution:
    def mergeKLists(self, lists):
        h = [(node.val, id(node), node) for node in lists if node is not None]
        if len(h) == 0:
            return None
        heapq.heapify(h)
        head = ListNode(0)
        cur = head
        while h:
            val, i, node = heapq.heappop(h)
            cur.next = node
            cur = node
            node = node.next
            if node:
                heapq.heappush(h, (node.val, id(node), node))
        return head.next


s = Solution()
print(s.mergeKLists([Util.createListNode([1, 4, 5]),
                     Util.createListNode([1, 3, 4]),
                     Util.createListNode([2, 6])]))
