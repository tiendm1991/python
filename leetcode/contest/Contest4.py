from datetime import datetime


class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        mod = 10 ** 9 + 7
        if n == 0:
            return 0
        def getKmp(pattern):
            n = len(pattern)
            if n == 0:
                return ''
            result = [0] * n
            i, j = 1, 0
            while i < n:
                if pattern[i] == pattern[j]:
                    result[i] = j + 1
                    i += 1
                    j += 1
                elif j == 0:
                    i += 1
                else:
                    j = result[j - 1]
            return result
        def containEvil(s, p, kmp):
            i, j = 0, 0
            while i < len(s):
                if s[i] == p[j]:
                    if j == len(p) - 1:
                        return True
                    i += 1
                    j += 1
                elif j == 0:
                    i += 1
                else:
                    j = kmp[j - 1]
            return False
        def convertNumToStr(num):
            s = ['a'] * n
            idx = n-1
            while num > 0:
                s[idx] = chr(num % 26 + 97)
                num //= 26
                idx -= 1
            return ''.join(s)
        def convertStrToNum(str):
            num = 0
            for c in str:
                num = num * 26 + ord(c) - 97
            return num

        kmp = getKmp(evil)
        count = 0
        begin = convertStrToNum(s1)
        end = convertStrToNum(s2)
        for x in range(begin, end + 1):
            s = convertNumToStr(x)
            if not containEvil(s, evil, kmp):
                count += 1
        return count % mod

pattern = Solution()
startTime = datetime.now()
print(pattern.findGoodStrings(8,"pzdanyao","wgpmtywi","sdka"))
print(datetime.now() - startTime)