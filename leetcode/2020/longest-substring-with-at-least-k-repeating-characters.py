import collections


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        if n < k:
            return 0
        if k == 1:
            return n
        d = collections.Counter(s)
        valid = {c: d[c] for c in d if d[c] >= k}
        notValid = {c: d[c] for c in d if d[c] < k}
        if len(notValid) == len(d):
            return 0
        if len(valid) == len(d):
            return n
        s += "#"
        res = 0
        candidate = ""
        for i, c in enumerate(s):
            if c not in valid:
                res = max(res, self.longestSubstring(candidate, k))
                candidate = ""
            else:
                candidate += c
        return res


s = Solution()
print(s.longestSubstring("ababacb", 3))
print(s.longestSubstring("bbaaacbd", 3))
print(s.longestSubstring("a", 1))
print(s.longestSubstring("bchhbbdefghiaaacb", 3))
print(s.longestSubstring("aaabbb", 3))
