class Solution:
    def escapeGhosts(self, ghosts, target) -> bool:
        s = set((g[0], g[1]) for g in ghosts)
        x = abs(target[0]) + abs(target[1])
        for g in s:
            if abs(g[0] - target[0]) + abs(g[1] - target[1]) <= x:
                return False
        return True


s = Solution()
print(s.escapeGhosts([[1, 0], [0, 3]], [0, 1]))
