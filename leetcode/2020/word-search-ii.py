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


class Solution:
    def findWords(self, board, words):
        trie = Trie()
        for w in words:
            trie.insert(w)
        m, n = len(board), len(board[0])

        def dfs(result, i, j, w, prevNode):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] == '.':
                return
            if board[i][j] not in prevNode.next:
                return
            # check valid word
            if prevNode.next[board[i][j]].is_end:
                result.add(w + board[i][j])
            # try
            tmp = board[i][j]
            curNode = prevNode.next[board[i][j]]
            board[i][j] = '.'
            # recursion
            dfs(result, i + 1, j, w + tmp, curNode)
            dfs(result, i - 1, j, w + tmp, curNode)
            dfs(result, i, j + 1, w + tmp, curNode)
            dfs(result, i, j - 1, w + tmp, curNode)
            # backtrack
            board[i][j] = tmp
            return

        result = set()
        w = ''
        for i in range(m):
            for j in range(n):
                dfs(result, i, j, w, trie.begin)
        return list(result)


s = Solution()
print(s.findWords([["a", "a"]], ["aaa"]))
