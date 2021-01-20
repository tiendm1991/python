# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from leetcode.Util import ListNode
from leetcode import Util
import math


class Solution:
    def splitListToParts(self, root: ListNode, k: int):
        cur, n = root, 0
        while cur is not None:
            n += 1
            cur = cur.next
        ans = [None] * k
        avg = n // k
        mod = n % k
        r = root
        cur = root
        i = 0
        j = 0
        while cur is not None:
            if i < avg + math.ceil(max(mod, 0) / k) - 1:
                i += 1
                cur = cur.next
            else:
                newNode = cur.next
                cur.next = None
                ans[j] = r
                j += 1
                i = 0
                mod -= 1
                cur = newNode
                r = newNode
        return ans


s = Solution()
print(s.splitListToParts(Util.createListNode([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3))
