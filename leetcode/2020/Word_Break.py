class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        n = len(s)
        if n == 0:
            return False
        dp = [False] * (n + 1)
        dp[0] = True
        d = set(wordDict)
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in d:
                    dp[i] = True
                    break
        return dp[n]


s = Solution()
print(s.wordBreak("leetcode", ["leet", "code"]))
print(s.wordBreak("applepenapple", ["apple", "pen"]))
print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
