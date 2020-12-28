class Node:
    def __init__(self):
        self.next = {}


class Trie:

    def __init__(self):
        self.begin = Node()

    def insert(self, x: int) -> None:
        i = 31
        prevNode = self.begin
        while i >= 0:
            mark = 1 << i
            bit = (x & mark) >> i
            if bit not in prevNode.next:
                prevNode.next[bit] = Node()
            prevNode = prevNode.next[bit]
            i -= 1

    def findMax(self, x: int):
        i = 31
        prevNode = self.begin
        res = 0
        while i >= 0:
            mark = 1 << i
            bit = (x & mark) >> i
            opBit = 1 - bit
            if opBit in prevNode.next:
                res |= mark
                prevNode = prevNode.next[opBit]
            else:
                prevNode = prevNode.next[bit]
            i -= 1
        return res


class Solution:
    def maximizeXor(self, nums, queries):
        for

s = Solution()
print(s.maximizeXor())
