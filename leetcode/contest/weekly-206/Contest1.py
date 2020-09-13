class Solution:
    def numSpecial(self, mat) -> int:
        m = len(mat)
        if m == 0:
            return 0
        n = len(mat[0])
        sr, sc = {}, set()
        bi, bj = [False] * m, [False] * n
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    if not bi[i]:
                        sr[i] = j
                        bi[i] = True
                    elif i in sr:
                        del sr[i]
                    if not bj[j]:
                        sc.add(j)
                        bj[j] = True
                    elif j in sc:
                        sc.remove(j)
        ans = 0
        for i in sr:
            if sr[i] in sc:
                ans += 1
        return ans


s = Solution()
print(s.numSpecial([[0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 1],
                    [0, 0, 0, 0, 1, 0, 0, 0],
                    [1, 0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 1, 1, 0, 0, 0, 0]]))
