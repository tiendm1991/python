class Solution:
    def threeEqualParts(self, a):
        def compare(a1, a2):
            n1, n2 = len(a1), len(a2)
            a1 = [0] * (max(n1, n2) - n1) + a1
            a2 = [0] * (max(n1, n2) - n2) + a2
            return a1 == a2

        n = len(a)
        count1 = a.count(1)
        if count1 == 0:
            return [0, n - 1]
        if count1 % 3:
            return [-1, -1]
        count1 //= 3
        s1, s2, c = -1, -1, 0
        for i in range(n):
            if a[i] == 1:
                c += 1
                if c == count1:
                    if s1 == -1:
                        s1 = i
                        c = 0
                    elif s2 == -1:
                        s2 = i
        zero = n - 1
        while zero >= 0 and a[zero] == 0:
            zero -= 1
        lastZeroes = n - 1 - zero
        x1 = a[:s1 + lastZeroes + 1]
        x2 = a[s1 + lastZeroes + 1:s2 + lastZeroes + 1]
        x3 = a[s2 + lastZeroes + 1:]
        if compare(x1, x2) and compare(x2, x3):
            return [s1 + lastZeroes, s2 + lastZeroes + 1]
        return [-1, -1]


s = Solution()
print(s.threeEqualParts([1, 0, 1, 0, 1]))
print(s.threeEqualParts([1, 0, 1, 1, 0]))
