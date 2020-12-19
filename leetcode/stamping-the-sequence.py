class Solution:
    def movesToStamp(self, stamp: str, target: str):
        n = len(target)
        m = len(stamp)

        def backtrack(cur, res):
            if cur == target:
                return res
            for i in range(n):
                if cur[i] != target[0]:
                    res.append(i)
                    x = cur[:i] + stamp + cur[i + m:]
                    if backtrack(x, res):
                        return res
                    res.pop()
            return []

        return backtrack("?" * n, [])


s = Solution()
print(s.movesToStamp("abc", "ababc"))
print(s.movesToStamp("abca", "aabcaca"))
