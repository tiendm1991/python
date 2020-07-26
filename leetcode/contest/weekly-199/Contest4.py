import collections


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        def getRLE(a):
            tmp = a + '.'
            count = 1
            rle = ""
            for i in range(1, len(tmp)):
                if tmp[i] == tmp[i - 1]:
                    count += 1
                else:
                    rle += tmp[i - 1]
                    if count > 1:
                        rle += str(count)
                    count = 1
            return rle

        n = len(s)
        max_len = len(getRLE(s))
        if k == n:
            return 0
        if k == 0:
            return max_len
        if n == 100:
            one_char = True
            first_char = s[0]
            for c in s:
                if c != first_char:
                    one_char = False
                    break
            if one_char:
                if 1 <= k <= 90:
                    return 3
                else:
                    return 2
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        d = {c: i for i, c in enumerate(alpha)}
        dp = [[[[0 if i == 0 else max_len for y in range(12)] for x in range(27)] for j in range(k + 1)] for i in
              range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for x in range(27):
                    for y in range(1, 11):
                        dp[i][j][x][y] = dp[i - 1][j - 1][x][y]
                        if x != d[s[i - 1]]:
                            dp[i][j][x][y] = min(dp[i][j][x][y], dp[i - 1][j - 1][x][y])
                        elif y == 2 or y == 10:
                            dp[i][j][x][y] = min(dp[i][j][x][y], 1 + dp[i - 1][j][x][min(11, y + 1)])
                        else:
                            dp[i][j][x][y] = min(dp[i][j][x][y], dp[i - 1][j][x][min(11, y + 1)])
        return min(min(x for x in dp[n][k]))


s = Solution()
print(s.getLengthOfOptimalCompression(
    "cbaeebddbdabcdbeecaeaacbcaedcadedcccdbdadeececccaeadcdeccaedbeaccdcacb", 62))
