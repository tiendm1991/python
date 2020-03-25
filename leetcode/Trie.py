from datetime import datetime, time
import heapq
import math
import random
import collections

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
        currentNode = self.begin
        while idx < len(word):
            ch = word[idx]
            if ch not in currentNode.next:
                break
            if idx == len(word) - 1:
                currentNode.next[ch].is_end = True
            idx += 1
            currentNode = currentNode.next[ch]
        for i in range(idx, len(word)):
            ch = word[i]
            currentNode.next[ch] = Node()
            if i == len(word) - 1:
                currentNode.next[ch].is_end = True
            currentNode = currentNode.next[ch]

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        idx = 0
        currentNode = self.begin
        while idx < len(word):
            ch = word[idx]
            if ch not in currentNode.next:
                break
            if idx == len(word) - 1:
                return currentNode.next[ch].is_end
            idx += 1
            currentNode = currentNode.next[ch]
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        idx = 0
        currentNode = self.begin
        while idx < len(prefix):
            ch = prefix[idx]
            if ch not in currentNode.next:
                break
            idx += 1
            currentNode = currentNode.next[ch]
        return idx == len(prefix)

obj = Trie()
obj.insert('apple')
obj.insert('april')
# print(obj.search('apple'))
# print(obj.startsWith('app'))
obj.insert('app')
print(obj.search('app'))

# s = Solution()
# startTime = datetime.now()
# print(s.countArrangement(2))
# print(datetime.now() - startTime)

