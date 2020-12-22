class Solution:
    def shortestSuperstring(self, a) -> str:
        def getDis(s1: str, s2: str):
            i = len(s2)
            while i > 0:
                if s1.endswith(s2[:i]):
                    return i
                i -= 1
            return 0

        n = len(a)
        if n == 1:
            return a[0]
        edges = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    edges[i][j] = getDis(a[i], a[j])
        dp = {}

        def tsp(t, c):
            if len(t) == 1:
                dp[(t, c)] = [0, [c]]
                return dp[(t, c)]
            if (t, c) in dp:
                return dp[(t, c)]
            res = [0, []]
            next_t = tuple(y for y in t if y != c)
            for i, x in enumerate(next_t):
                res_next = tsp(next_t, x)
                if res_next[0] + edges[x][c] >= res[0]:
                    res = [res_next[0] + edges[x][c], res_next[1] + [c]]
            dp[(t, c)] = res
            return res

        ans = [0, []]
        b = tuple(range(n))
        for x in range(n):
            y = tsp(b, x)
            if y[0] >= ans[0]:
                ans = y
        ans = ans[1]
        res = a[ans[0]]
        for i in range(1, n):
            res += a[ans[i]][edges[ans[i - 1]][ans[i]]:]
        return res


s = Solution()
print(s.shortestSuperstring(["catg", "ctaagt", "gcta", "ttca", "atgcatc"]))
print(s.shortestSuperstring(["alex", "loves", "leetcode"]))
