class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        digits = {str(x) for x in range(10)}
        curLen = 0
        i = 0
        while i < len(s):
            if s[i] in digits:
                curLen *= int(s[i])
            else:
                curLen += 1
            if curLen >= k:
                break
            i += 1
        while i >= 0:
            if s[i] in digits:
                d = curLen // int(s[i])
                curLen = d
                k = (k - 1) % d + 1
            else:
                if curLen == k:
                    return s[i]
                else:
                    curLen -= 1
            i -= 1
        return ''


s = Solution()
# print(s.decodeAtIndex("a2b3c4d5e6f7g8h9", 623529))
# print(s.decodeAtIndex("leet2code3", 20))
print(s.decodeAtIndex("leet2code3", 10))
