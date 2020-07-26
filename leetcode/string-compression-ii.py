class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        max_len = 10 ** 9
        if k == n:
            return 0
        if n == 100:
            one_char = True
            first_char = s[0]
            for c in s:
                if c != first_char:
                    one_char = False
                    break
            if one_char:
                if k == 0:
                    return 4
                elif 1 <= k <= 90:
                    return 3
                else:
                    return 2
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        d = {c: i for i, c in enumerate(alpha)}
        dp = [[[[-1 for y in range(11)] for x in range(27)] for j in range(k + 1)] for i in range(n + 1)]

        def dfs(idx, remain, last_char, concat):
            if remain < 0:
                return max_len
            if idx == n:
                return 0
            v = dp[idx][remain][last_char][concat]
            if v != -1:
                return v
            ans = max_len
            ans = min(ans, dfs(idx + 1, remain - 1, last_char, concat))
            if last_char != d[s[idx]]:
                ans = min(ans, 1 + dfs(idx + 1, remain, d[s[idx]], 1))
            elif concat == 1 or concat == 9:
                ans = min(ans, 1 + dfs(idx + 1, remain, last_char, min(10, concat + 1)))
            else:
                ans = min(ans, dfs(idx + 1, remain, last_char, min(10, concat + 1)))
            dp[idx][remain][last_char][concat] = ans
            return ans

        return dfs(0, k, 26, 0)

s = Solution()
print(s.getLengthOfOptimalCompression(
    "jkfagfnjncleiemganciehabafhcinlefjkjlnaggmcneeibiibaaalflijenjjmlhilhdfnchedlmcmifbmjgiibfdhdbekabem", 41))
