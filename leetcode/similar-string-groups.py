class Solution:
    def numSimilarGroups1(self, A) -> int:
        a = list(set(A))
        n = len(a)
        if n == 1:
            return 1
        edges = []
        p = [i for i in range(n)]

        def connected(s1, s2):
            if len(s1) != len(s2) or len(s1) < 2:
                return False
            pre = -1
            count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    count += 1
                    if count == 1:
                        pre = i
                    elif count > 2 or s1[pre] != s2[i] or s1[i] != s2[pre]:
                        return False
            return True

        def find(u):
            if u != p[u]:
                p[u] = find(p[u])
            return p[u]

        for i in range(n - 1):
            for j in range(i + 1, n):
                if connected(a[i], a[j]):
                    edges.append((i, j))

        for e in edges:
            rx, ry = find(e[0]), find(e[1])
            if rx < ry:
                p[ry] = rx
            elif ry < rx:
                p[rx] = ry
        ans = set()
        for i in p:
            ans.add(find(i))
        return len(ans)

    def numSimilarGroups(self, A) -> int:
        a = list(set(A))
        n = len(a)
        if n == 1:
            return 1

        def connected(s1, s2):
            if len(s1) != len(s2):
                return False
            pre = -1
            count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    count += 1
                    if count == 1:
                        pre = i
                    elif count > 2 or s1[pre] != s2[i] or s1[i] != s2[pre]:
                        return False
            return True

        visited = [False] * n

        def dfs(u):
            visited[u] = True
            for v in range(n):
                if not visited[v] and connected(a[u], a[v]):
                    dfs(v)

        ans = 0
        for i in range(n):
            if not visited[i]:
                ans += 1
                dfs(i)
        return ans


s = Solution()
print(s.numSimilarGroups(
    ["ajdidocuyh", "djdyaohuic", "ddjyhuicoa", "djdhaoyuic", "ddjoiuycha", "ddhoiuycja", "ajdydocuih", "ddjiouycha",
     "ajdydohuic", "ddjyouicha"]))
print(s.numSimilarGroups(["nmiwx", "mniwx", "wminx", "mnixw", "xnmwi"]))
