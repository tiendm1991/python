class Solution:
    def arrayStringsAreEqual(self, word1, word2) -> bool:
        return ''.join(word1) == ''.join(word2)


s = Solution()
print(s.arrayStringsAreEqual(["a", "cb"], ["ab", "c"]))
