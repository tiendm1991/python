class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            if s == '':
                return False
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        result = []
        a = []
        remain = s
        remain += '*'

        def helper(result, a, remain):
            if remain == '*':
                result.append(a[::])
                return
            for i in range(1, len(remain) + 1):
                x = remain[0:i]
                if isPalindrome(x):
                    a.append(x)
                    helper(result, a, remain[i:])
                    del a[-1]

        helper(result, a, remain)
        return result
