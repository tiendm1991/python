class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        d = {}
        for i in range(n):
            d[i] = {i}
            sub = s[i]
            rev = s[i]
            for j in range(i + 1, n):
                sub += s[j]
                rev = s[j] + rev
                if sub == rev:
                    d[i].add(j)
        for i in d[0]:
            if i >= n - 2:
                continue
            for j in d[i + 1]:
                if j == n - 1:
                    continue
                if n - 1 in d[j + 1]:
                    return True
        return False


s = Solution()
print(s.checkPartitioning("abcbdd"))
print(s.checkPartitioning("bcbddxy"))
