class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 1:
            return 5
        pre = [1] * 5
        ans = [0] * 5
        for i in range(n - 1):
            ans = [0] * 5
            ans[0] = sum(pre)
            ans[1] = sum(pre[1:])
            ans[2] = sum(pre[2:])
            ans[3] = sum(pre[3:])
            ans[4] = sum(pre[4:])
            pre = ans
        return sum(ans)


s = Solution()
print(s.countVowelStrings(1))
print(s.countVowelStrings(2))
