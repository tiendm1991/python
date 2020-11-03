class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        _set = set()
        ans = 0
        for i in range(m):
            for j in range(n):
                if s[i] == t[j]:
                    k = 1
                    while i + k < m and j + k < n and s[i + k] == t[j + k]:
                        k += 1
                    if i + k < m and j + k < n:
                        ans += 1
                        k += 1
                        while i + k < m and j + k < n and s[i + k] == t[j + k]:
                            ans += 1
                            k += 1
                else:
                    ans += 1
                    k = 1
                    while i + k < m and j + k < n and s[i + k] == t[j + k]:
                        ans += 1
                        k += 1

        return ans


s = Solution()
print(s.countSubstrings("bab", "bbb"))
# print(s.countSubstrings("aa", "bb"))
