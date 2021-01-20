class Solution:
    def isAlienSorted(self, words, order: str) -> bool:
        d = {c: i for i, c in enumerate(order)}

        def valid(w1: str, w2: str):
            i = 0
            while i < len(w1) and i < len(w2):
                if d[w1[i]] < d[w2[i]]:
                    return True
                elif d[w1[i]] > d[w2[i]]:
                    return False
                i += 1
            return i == len(w1)

        n = len(words)
        if n == 1:
            return True
        for i in range(1, n):
            if not valid(words[i - 1], words[i]):
                return False
        return True


s = Solution()
print(s.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
print(s.isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))
