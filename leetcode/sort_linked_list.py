from leetcode.Util import ListNode
from leetcode import Util


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def mergeSort(node: ListNode):
            if node is None or node.next is None:
                return node
            pre, slow, fast = None, node, node
            while fast is not None and fast.next is not None:
                pre = slow
                slow = slow.next
                fast = fast.next.next
            pre.next = None
            n1 = mergeSort(node)
            n2 = mergeSort(slow)
            return merge(n1, n2)

        def merge(node1: ListNode, node2: ListNode):
            if node1 is None:
                return node2
            if node2 is None:
                return node1
            cur1, cur2 = node1, node2
            h = ListNode(0)
            cur = h
            while cur1 is not None and cur2 is not None:
                if cur1.val <= cur2.val:
                    cur.next = cur1
                    cur1 = cur1.next
                else:
                    cur.next = cur2
                    cur2 = cur2.next
                cur = cur.next
            if cur1 is None:
                cur.next = cur2
            else:
                cur.next = cur1
            return h.next

        return mergeSort(head)


s = Solution()
print(s.sortList(Util.createListNode([-1, 5, 3, 4, 0])))
