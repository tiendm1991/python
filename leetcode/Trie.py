class Node:
    def __init__(self):
        self.is_end = False
        self.next = {}  # you could use an array and char indices, but a dict is so much more elegant


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.begin = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        idx = 0
        prevNode = self.begin
        while idx < len(word):
            ch = word[idx]
            if ch not in prevNode.next:
                break
            idx += 1
            prevNode = prevNode.next[ch]
        if idx == len(word):
            prevNode.is_end = True
        else:
            for i in range(idx, len(word)):
                ch = word[i]
                curNode = Node()
                prevNode.next[ch] = curNode
                prevNode = curNode
            prevNode.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        idx = 0
        prevNode = self.begin
        while idx < len(word):
            ch = word[idx]
            if ch not in prevNode.next:
                break
            idx += 1
            prevNode = prevNode.next[ch]
        if idx == len(word):
            return prevNode.is_end
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        idx = 0
        prevNode = self.begin
        while idx < len(prefix):
            ch = prefix[idx]
            if ch not in prevNode.next:
                break
            idx += 1
            prevNode = prevNode.next[ch]
        return idx == len(prefix)


obj = Trie()
obj.insert('app')
obj.insert('apple')
obj.insert('april')
# print(obj.search('apple'))
# print(obj.startsWith('app'))
print(obj.search('april'))