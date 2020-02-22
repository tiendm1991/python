class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def isPalidrome(s, end):
            return s[:end+1] == s[end::-1]

        def findMaxPalindrome(s):
            for i in range(len(s) - 1, 0, -1):
                if isPalidrome(s, i):
                    return i
            return 0

        idx = findMaxPalindrome(s)
        add = ''
        for i in range(len(s) - 1, idx, -1):
            add += s[i]
        return add + s
s = Solution()
print(s.shortestPalindrome('aacecaaa'))
