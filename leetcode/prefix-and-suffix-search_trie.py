class Node:
    def __init__(self):
        self.next = {}  # you could use an array and char indices, but a dict is so much more elegant
        self.prev = {}  # you could use an array and char indices, but a dict is so much more elegant
        self.preIndex = []
        self.sufIndex = set()


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pre = Node()
        self.suf = Node()

    def insertPre(self, word: str, pos) -> None:
        """
        Inserts a word into the trie.
        """
        idx = 0
        cur = self.pre
        while idx < len(word):
            ch = word[idx]
            if ch not in cur.next:
                break
            idx += 1
            cur = cur.next[ch]
            cur.preIndex.append(pos)

        for i in range(idx, len(word)):
            ch = word[i]
            nextNode = Node()
            cur.next[ch] = nextNode
            nextNode.preIndex.append(pos)
            cur = nextNode

    def insertSuf(self, word: str, pos) -> None:
        """
        Inserts a word into the trie.
        """
        idx = len(word) - 1
        cur = self.suf
        while idx >= 0:
            ch = word[idx]
            if ch not in cur.prev:
                break
            idx -= 1
            cur = cur.prev[ch]
            cur.sufIndex.add(pos)

        for i in range(idx, -1, -1):
            ch = word[i]
            prevNode = Node()
            cur.prev[ch] = prevNode
            prevNode.sufIndex.add(pos)
            cur = prevNode

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        idx = 0
        cur = self.pre
        while idx < len(prefix):
            ch = prefix[idx]
            if ch not in cur.next:
                break
            idx += 1
            cur = cur.next[ch]
        if idx == len(prefix):
            return cur.preIndex
        return []

    def endsWith(self, suffix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        idx = len(suffix) - 1
        cur = self.suf
        while idx >= 0:
            ch = suffix[idx]
            if ch not in cur.prev:
                break
            idx -= 1
            cur = cur.prev[ch]
        if idx == -1:
            return cur.sufIndex
        return set()

    def search(self, prefix, suffix):
        p, s = self.startsWith(prefix), self.endsWith(suffix)
        if len(p) == 0 or len(s) == 0:
            return -1
        for i in range(len(p) - 1, -1, -1):
            if p[i] in s:
                return p[i]
        return -1


class WordFilter:

    def __init__(self, words):
        self.trie = Trie()
        for i, w in enumerate(words):
            self.trie.insertPre(w, i)
            self.trie.insertSuf(w, i)

    def f(self, prefix: str, suffix: str) -> int:
        return self.trie.search(prefix, suffix)


obj = WordFilter(
    ["cabaabaaaa", "ccbcababac", "bacaabccba", "bcbbcbacaa", "abcaccbcaa",
     "accabaccaa", "cabcbbbcca", "ababccabcb", "caccbbcbab", "bccbacbcba"])
print(obj.f("cab", "bbcca"))
