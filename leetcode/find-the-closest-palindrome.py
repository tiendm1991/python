from  datetime import datetime
import functools
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        x = int(n)
        if x < 10:
            return str(x - 1) if x > 0 else '0'
        l = len(n)
        s = [c for c in n]
        candidate = set()
        if s[0] == '1':
            candidate.add(int('9' * (l-1)))
        if s[0] == '9':
            candidate.add(int('1' + '0' * l) + 1)
        i, j = 0, l-1
        palindrome = True
        while i < j:
            if s[j] != s[i]:
                palindrome = False
            s[j] = s[i]
            i += 1
            j -= 1
        if palindrome:
            i = l // 2
            if s[i] == '0':
                s[i] = '1'
            else:
                s[i] = str(int(s[i]) - 1)
            if l % 2 == 0:
                s[i - 1] = s[i]
            candidate.add(int(''.join(s)))
        else:
            candidate.add(int(''.join(s)))
            midIdx = l//2
            s1 = s[::]
            mid = int(s[midIdx])
            if mid < 9:
                s1[midIdx] = str(mid + 1)
            if mid > 0:
                s[midIdx] = str(mid - 1)
            if l % 2 == 0:
                s1[midIdx-1] = s1[midIdx]
                s[midIdx-1] = s[midIdx]
            candidate.add(int(''.join(s1)))
            candidate.add(int(''.join(s)))
        _min = float('inf')
        result = ''
        for c in candidate:
            if abs(c - x) < _min or abs(c - x) == _min and c < int(result):
                _min = abs(c - x)
                result = str(c)
        return result

s = Solution()
startTime = datetime.now()
print(s.nearestPalindromic("1213"))
print(datetime.now() - startTime)