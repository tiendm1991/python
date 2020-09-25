class Solution:
    def accountsMerge(self, accounts):
        n = len(accounts)
        d = {i: [] for i in range(n)}
        accounts.sort()
        for i in range(n - 1):
            si = set(accounts[i][1:])
            for j in range(i + 1, n):
                if accounts[i][0] != accounts[j][0]:
                    continue
                sj = set(accounts[j][1:])
                if si.intersection(sj):
                    d[i].append(j)
                    d[j].append(i)

        def dfs(u):
            visited[u] = True
            mails = set(accounts[u][1:])
            for v in d[u]:
                if not visited[v]:
                    mails = mails.union(dfs(v))
            return mails

        ans = []
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                a = [accounts[i][0]]
                a += sorted(dfs(i))
                ans.append(a)
        return ans


s = Solution()
print(s.accountsMerge([["David", "David5@m.co", "David8@m.co"],
                       ["David", "David1@m.co", "David1@m.co", "David8@m.co"],
                       ["David", "David0@m.co", "David0@m.co", "David5@m.co"]]))
