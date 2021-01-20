class Solution:
    def unhappyFriends(self, n: int, preferences, pairs) -> int:
        p = {}
        d = {}
        for i, pair in enumerate(pairs):
            p[pair[0]] = i
            p[pair[1]] = i

        for i, prefer in enumerate(preferences):
            d[i] = {}
            for j, u in enumerate(prefer):
                d[i][u] = j

        def isUnHappy(x):
            y = sum(pairs[p[x]]) - x
            for j, u in enumerate(preferences[x]):
                if u == y:
                    break
                v = sum(pairs[p[u]]) - u
                if d[u][x] < d[u][v]:
                    return True
            return False

        ans = 0
        for x in range(n):
            if isUnHappy(x):
                ans += 1
        return ans


s = Solution()
print(s.unhappyFriends(4,
                       [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]],
                       [[1, 3], [0, 2]]))
