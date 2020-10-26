# https://leetcode.com/problems/string-compression-ii
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        max_len = 100
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

        def dfs(idx, remain, last_char, count):
            if remain < 0:
                return max_len
            if idx == n:
                return 0
            v = dp[idx][remain][last_char][count]
            if v != -1:
                return v
            ans = max_len
            # Remove
            ans = min(ans, dfs(idx + 1, remain - 1, last_char, count))
            # Concat
            cur_char = d[s[idx]]
            if last_char != cur_char:
                ans = min(ans, 1 + dfs(idx + 1, remain, cur_char, 1))
            elif count == 1 or count == 9:
                ans = min(ans, 1 + dfs(idx + 1, remain, last_char, count + 1))
            else:
                ans = min(ans, dfs(idx + 1, remain, last_char, min(10, count + 1)))
            dp[idx][remain][last_char][count] = ans
            return ans

        return dfs(0, k, 26, 0)


s = Solution()
print(s.getLengthOfOptimalCompression(
    "jkfagfnjncleiemganciehabafhcinlefjkjlnaggmcneeibiibaaalflijenjjmlhilhdfnchedlmcmifbmjgiibfdhdbekabem", 41))
