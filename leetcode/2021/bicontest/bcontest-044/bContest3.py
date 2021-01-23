class Solution:
    def decode(self, encoded):
        s = 0
        for x in range(1, len(encoded) + 2):
            s ^= x
        a = [encoded[0]]
        for i in range(1, len(encoded)):
            a.append(a[-1] ^ encoded[i])
        first = s
        for x in a:
            first ^= x
        res = [first]
        for x in encoded:
            res.append(res[-1] ^ x)
        return res


s = Solution()
print(s.decode([3, 1]))
print(s.decode([6, 5, 4, 6]))
