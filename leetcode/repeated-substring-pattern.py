class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n < 2:
            return False
        p = [0] * n
        i, j = 1, 0
        while i < n:
            if s[i] == s[j]:
                p[i] = j+1
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = p[j-1]
        for i in range(1, n):
            if i != 0 and n % i == 0 and p[-1] == n - i:
                return True
        return False

s = Solution()
print(s.repeatedSubstringPattern("aabaabaab"))
print(s.repeatedSubstringPattern("aabaabaaa"))