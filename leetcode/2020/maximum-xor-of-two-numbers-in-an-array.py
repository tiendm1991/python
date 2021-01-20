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
    def findMaximumXOR(self, nums) -> int:
        res = 0
        trie = Trie()
        for x in nums:
            trie.insert(x)
        for x in nums:
            res = max(res, trie.findMax(x))
        return res


s = Solution()
print(s.findMaximumXOR([3, 10, 5, 25, 2, 8]))
# 000011 3
# 001010 10
# 000101 5
# 011001 25
# 000010 2
# 001000 8
