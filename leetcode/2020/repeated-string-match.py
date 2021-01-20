class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        m, n = len(a), len(b)
        time = -1
        for i in range(m - 1, -1, -1):
            if a[i] == b[0]:
                time = (i + n) // m
                if (i + n) % m != 0:
                    time += 1
                break
        repeat = ""
        for i in range(1, time + 1):
            repeat += a
            if b in repeat:
                return i
        return -1


s = Solution()
print(s.repeatedStringMatch("abcd", "cdabcdab"))
