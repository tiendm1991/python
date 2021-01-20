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
        nums = sorted(set(nums))
        n, nq = len(nums), len(queries)
        queries = sorted([(q, i) for i, q in enumerate(queries)], key=lambda q: q[0][1])
        res = [-1] * nq
        trie = Trie()
        i = 0
        for q, idx in queries:
            x, m = q
            if m < nums[0]:
                continue
            while i < n and nums[i] <= m:
                trie.insert(nums[i])
                i += 1
            res[idx] = trie.findMax(x)
        return res


s = Solution()
print(s.maximizeXor([0, 1, 2, 3, 4], [[3, 1], [1, 3], [5, 6]]))
print(s.maximizeXor([5, 2, 4, 6, 6, 3], [[12, 4], [8, 1], [6, 3]]))
