class Solution:
    def queryString(self, S: str, N: int) -> bool:
        if N > 10 ** 6:
            return False
        n = len(S)
        s = set()
        res = 0
        for i in range(n):
            x = 0
            for j in range(i, min(i + 20, n)):
                c = int(S[j])
                x = x << 1 | c
                if 1 <= x <= N and x not in s:
                    res += 1
                s.add(x)

        return res == N


s = Solution()
print(s.queryString("0110", 3))
