class Solution:
    def pyramidTransition(self, bottom: str, allowed) -> bool:
        d = {}
        for w in allowed:
            k = w[:2]
            if k not in d:
                d[k] = {w[2]}
            else:
                d[k].add(w[2])

        def dfs(a, i, cur):
            n = len(a)
            if n == 1:
                return True
            if i == n - 1:
                return dfs(cur, 0, "")
            k = a[i: i + 2]
            if k not in d:
                return False
            for x in d[k]:
                if dfs(a, i + 1, cur + x):
                    return True
            return False

        return dfs(bottom, 0, "")


s = Solution()
print(s.pyramidTransition("AABA", ["AAA", "AAB", "ABA", "ABB", "BAC"]))
