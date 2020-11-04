class Solution:
    def splitIntoFibonacci(self, s: str):
        maxVal = 2 ** 31 - 1
        n = len(s)
        if n < 3:
            return False

        def backtrack(arr, start):
            if start == n:
                if len(arr) > 2:
                    return arr
                return []
            if s[start] == '0' and (len(arr) < 2 or arr[-1] + arr[-2] == 0):
                return backtrack(arr + [0], start + 1)
            for end in range(start + 1, n + 1):
                x = int(s[start: end])
                if x >= maxVal:
                    continue
                if len(arr) < 2 or arr[-1] + arr[-2] == x:
                    a = backtrack(arr + [x], end)
                    if a:
                        return a
            return []

        return backtrack([], 0)


s = Solution()
print(s.splitIntoFibonacci("112358130"))
print(s.splitIntoFibonacci("0112"))
print(s.splitIntoFibonacci("123456579"))
