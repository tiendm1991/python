import random
import bisect


class Solution:
    def numSubmat_n4(self, mat) -> int:
        m = len(mat)
        if m == 0:
            return 0
        n = len(mat[0])
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        result = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + mat[i - 1][j - 1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if mat[i - 1][j - 1] == 0:
                    continue
                for k in range(m):
                    for l in range(n):
                        x, y = i + k, j + l
                        if x <= m and y <= n:
                            if dp[x][y] - dp[i - 1][y] - dp[x][j - 1] + dp[i - 1][j - 1] == (k + 1) * (l + 1):
                                result += 1
        return result

    def numSubmat_n3(self, mat) -> int:
        m = len(mat)
        if m == 0:
            return 0
        n = len(mat[0])
        result = 0
        for i in range(m):
            a = [0] * n
            for j in range(i, m):
                for x in range(n):
                    a[x] += mat[j][x]
                check = j - i + 1
                aCheck = [0 if x != check else 1 for x in a]
                aCheck.append(0)
                start = -1
                for k in range(n + 1):
                    if aCheck[k] == 1:
                        if start == -1:
                            start = k
                        continue
                    elif start != -1:
                        count = k - start
                        result += count * (count + 1) // 2
                        start = -1
        return result


s = Solution()
print(s.numSubmat_n3([[1, 0, 1],
                      [1, 1, 0],
                      [1, 1, 0]]))
print(s.numSubmat_n3([[0, 1, 1, 0],
                      [0, 1, 1, 1],
                      [1, 1, 1, 0]]))
print(s.numSubmat_n3([[1, 1, 1, 1, 1, 1]]))
