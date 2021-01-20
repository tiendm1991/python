class Node:
    def __init__(self):
        self.next = {}


class Trie:
    def __init__(self):
        self.begin = Node()

    def insert(self, word):
        cur = self.begin
        i = 0
        while i < len(word) and word[i] in cur.next:
            cur = cur.next[word[i]]
            i += 1

        while i < len(word):
            newNode = Node()
            cur.next[word[i]] = newNode
            cur = newNode
            i += 1

    def count(self):
        def dfs(node: Node):
            if len(node.next) == 0:
                return [1, 1]
            ans = [0, 0]
            for w in node.next:
                r = dfs(node.next[w])
                ans[1] += r[1]
                ans[0] += r[0]
            ans[0] += ans[1]
            return ans

        res = dfs(self.begin)
        return res[0]  # return res[0] - res[1] + res[1](number of #)


class Solution:
    def minimumLengthEncoding1(self, words) -> int:
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        words = sorted(words, key=lambda w: len(w), reverse=True)
        n = len(words)
        p = [i for i in range(n)]
        for i in range(n - 1):
            for j in range(i + 1, n):
                if words[i].endswith(words[j]):
                    ri = find(i)
                    p[j] = ri
        ans = 0
        s = set(p)
        for idx in s:
            ans += len(words[idx])
        return ans + len(s)

    def minimumLengthEncoding(self, words) -> int:
        t = Trie()
        words = [w[::-1] for w in words]
        for w in words:
            t.insert(w)
        return t.count()


s = Solution()
print(s.minimumLengthEncoding(["time", "atime", "btime"]))
print(s.minimumLengthEncoding(["time", "me", "bell"]))
