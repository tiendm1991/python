class Solution:
    def expressiveWords(self, s: str, words) -> int:
        ns = len(s)

        def check(x):
            n = len(x)
            if n > ns:
                return False
            i, j = 0, 0
            while i < n:
                if j >= ns or x[i] != s[j]:
                    return False
                tmp1 = j + 1
                while tmp1 < ns and s[tmp1] == s[j]:
                    tmp1 += 1
                tmp2 = i + 1
                while tmp2 < n and x[tmp2] == x[i]:
                    tmp2 += 1
                if tmp1 - j < tmp2 - i or (tmp1 - j > tmp2 - i and tmp1 - j == 2):
                    return False
                j = tmp1
                i = tmp2
            return j == ns

        ans = 0
        for x in words:
            if check(x):
                ans += 1
        return ans


s = Solution()
print(s.expressiveWords("heeellooo", ["hello", "hi", "helo"]))
