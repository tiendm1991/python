class Solution:
    def flipgame(self, fronts, backs) -> int:
        n = len(fronts)
        prohibit = {fronts[i] for i in range(n) if fronts[i] == backs[i]}
        ans = 2001
        for i in range(n):
            if fronts[i] not in prohibit:
                ans = min(ans, fronts[i])
            if backs[i] not in prohibit:
                ans = min(ans, backs[i])
        return ans if ans < 2001 else 0


s = Solution()
print(s.flipgame([1, 2, 4, 4, 7], [1, 3, 4, 1, 3]))
