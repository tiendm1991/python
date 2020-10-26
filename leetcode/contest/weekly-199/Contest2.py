class Solution:
    def minFlips(self, target: str) -> int:
        n = len(target)
        ans = 0
        for i in range(n):
            if (target[i] == '0' and ans % 2 == 1) or (target[i] == '1' and ans % 2 == 0):
                ans += 1
        return ans


s = Solution()
print(s.minFlips("001011101"))
