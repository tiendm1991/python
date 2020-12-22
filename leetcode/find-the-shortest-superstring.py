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

        # dp is memories of sub problems with 2 element: max_value and path
        dp = {}

        def tsp(t, c):
            if len(t) == 1:
                dp[(t, c)] = [0, [c]]
                return dp[(t, c)]
            if (t, c) in dp:
                return dp[(t, c)]
            r = [0, []]
            sub_t = tuple(y for y in t if y != c)
            for i, k in enumerate(sub_t):
                sub_res = tsp(sub_t, k)
                if sub_res[0] + edges[k][c] >= r[0]:
                    r = [sub_res[0] + edges[k][c], sub_res[1] + [c]]
            dp[(t, c)] = r
            return r

        ans = [0, []]
        b = tuple(range(n))
        for x in range(n):
            y = tsp(b, x)
            if y[0] >= ans[0]:
                ans = y
        path = ans[1]
        res = a[path[0]]
        for i in range(1, n):
            res += a[path[i]][edges[path[i - 1]][path[i]]:]
        return res


s = Solution()
print(s.shortestSuperstring(["catg", "ctaagt", "gcta", "ttca", "atgcatc"]))
print(s.shortestSuperstring(["alex", "loves", "leetcode"]))
