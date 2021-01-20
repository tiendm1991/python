class Solution:
    def expressiveWords(self, s: str, words) -> int:
        ns = len(s)

        def check2(x):
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

        def count(x):
            x += '#'
            start = 0
            ans = []
            for i in range(1, len(x)):
                if x[i] != x[i - 1]:
                    ans.append([x[i - 1], i - start])
                    start = i
            return ans

        a = count(s)

        def check(x):
            b = count(x)
            if len(a) != len(b):
                return False
            for i in range(len(a)):
                if a[i][0] != b[i][0]:
                    return False
                if b[i][1] > a[i][1] or (a[i][1] > b[i][1] and a[i][1] == 2):
                    return False
            return True

        ans = 0
        for st in words:
            if check(st):
                ans += 1
        return ans


s = Solution()
print(s.expressiveWords("heeellooo", ["hello", "hi", "helo"]))
