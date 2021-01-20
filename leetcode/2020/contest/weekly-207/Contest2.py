class Solution:
    ans = 0

    def maxUniqueSplit(self, s: str) -> int:
        _set = set()

        def backtrack(s):
            if s == '':
                self.ans = max(self.ans, len(_set))
                return
            for i in range(1, len(s) + 1):
                if s[:i] in _set:
                    continue
                _set.add(s[:i])
                backtrack(s[i:])
                _set.remove(s[:i])
            return

        backtrack(s)
        return self.ans


s = Solution()
print(s.maxUniqueSplit("ababccc"))
