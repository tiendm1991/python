import string


class Solution:
    def getSmallestString1(self, n: int, k: int) -> str:
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

    def getSmallestString(self, n: int, k: int) -> str:
        d = {i + 1: string.ascii_lowercase[i] for i in range(26)}
        a = [1] * n
        k -= n
        i = n - 1
        while k > 0:
            x = min(k, 25)
            a[i] += x
            i -= 1
            k -= x

        return ''.join([d[c] for c in a])


s = Solution()
print(s.getSmallestString(3, 27))
print(s.getSmallestString(5, 73))
