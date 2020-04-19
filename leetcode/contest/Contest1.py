import collections


class Solution:
    def reformat(self, s: str) -> str:
        if len(s) < 2:
            return s
        digits = [c for c in s if c in '0123456789']
        letters = [c for c in s if c not in '0123456789']
        n1, n2 = len(digits), len(letters)
        if abs(n1 - n2) > 1:
            return ''
        result = ''
        if n1 < n2:
            result += letters[0]
            for i in range(n1):
                result += digits[i] + letters[i+1]
        elif n1 > n2:
            result += digits[0]
            for i in range(n2):
                result += letters[i] + digits[i+1]
        else:
            for i in range(n1):
                result += letters[i] + digits[i]
        return result

s = Solution()
print(s.reformat("ab123"))