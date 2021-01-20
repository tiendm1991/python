class Solution:
    def superpalindromesInRange(self, l: str, r: str) -> int:
        candidate = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in range(1, 10000):
            candidate.append(str(i) + str(i)[::-1])
            for j in range(10):
                candidate.append(str(i) + str(j) + str(i)[::-1])
        l, r = int(l), int(r)
        res = 0
        for i in candidate:
            x = int(i)
            square = x ** 2
            s = str(square)
            if (len(s) == 1 or s == s[::-1]) and l <= square <= r:
                res += 1
        return res


s = Solution()
print(s.superpalindromesInRange("4", "1000"))
