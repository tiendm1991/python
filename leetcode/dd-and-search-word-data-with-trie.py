from datetime import datetime, time
import heapq
import math
import random
import collections


class Node:
        def __init__(self):
            self.is_end = False
            self.next = {}  # you could use an array and char indices, but a dict is so much more elegant

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.begin = Node()


    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
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
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def check(w, currentNode: Node, idx):
            if idx == len(w) or not currentNode.next:
                return False
            ch = w[idx]
            if ch != '.':
                if ch not in currentNode.next:
                    return False
                if idx == len(w) - 1:
                    return currentNode.next[ch].is_end
                return check(w, currentNode.next[ch], idx + 1)
            else:
                for chNext in currentNode.next:
                    if idx == len(w) - 1:
                        if currentNode.next[chNext].is_end:
                            return True
                    elif check(w, currentNode.next[chNext], idx + 1):
                        return True
            return False
        return check(word, self.begin, 0)



obj = WordDictionary()
obj.addWord('at')
obj.addWord('and')
obj.addWord('an')
obj.addWord('add')
obj.addWord('bat')
print(obj.search('.'))

# s = Solution()
# startTime = datetime.now()
# print(s.diameterOfBinaryTree(Util.createTree([])))
# print(datetime.now() - startTime)

