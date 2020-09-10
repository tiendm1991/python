class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        def extendPalidrome(j, k):
            a = 0
            while j >= 0 and k < n:
                if s[j] != s[k]:
                    break
                a += 1
                j -= 1
                k += 1
            return a

        for i in range(n):
            ans += extendPalidrome(i, i)
        for i in range(n - 1):
            ans += extendPalidrome(i, i + 1)
        return ans


s = Solution()
print(s.countSubstrings("aaa"))
