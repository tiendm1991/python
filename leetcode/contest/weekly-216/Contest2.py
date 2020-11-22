import string


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        chars = string.ascii_lowercase
        div, mod = k // 26, k % 26
        a = [0] * (n - div - 1) + [mod] + [26] * div
        i, j = 0, n - div - 1
        while a[i] == 0:
            if a[j] > 1:
                a[i] += 1
                a[j] -= 1
                i += 1
            else:
                j += 1
        return ''.join([chars[x - 1] for x in a])


s = Solution()
print(s.getSmallestString(5, 73))
