import functools
from datetime import datetime, time
import math
import bisect
import random
import collections

from testcases.cebu import Util
from testcases.cebu.Util import TreeNode


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        self.child = None


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        cur = head
        stack = []
        while cur.next != None or cur.child != None or stack:
            if cur.next == None:
                if cur.child == None:
                    branch = stack.pop()
                    nextTmp = branch.next
                    branch.next = branch.child
                    branch.next.prev = branch
                    branch.child = None
                    cur.next = nextTmp
                    if nextTmp:
                        nextTmp.prev = cur
                        cur = nextTmp
                else:
                    stack.append(cur)
                    cur = cur.child
            else:
                if cur.child == None:
                    cur = cur.next
                else:
                    stack.append(cur)
                    cur = cur.child
        return head


s = Solution()
startTime = datetime.now()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node10 = Node(10)
node11 = Node(11)
node12 = Node(12)
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3
node3.child = node7
node4.next = node5
node5.prev = node4
node5.next = node6
node6.prev = node5
node7.next = node8
node8.prev = node7
node8.child = node11
node8.next = node9
node9.prev = node8
node9.next = node10
node10.prev = node9
node11.next = node12
node12.prev = node11
print(s.flatten(node1))
print(datetime.now() - startTime)
