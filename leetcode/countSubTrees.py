class Solution:
    def countSubTrees(self, n: int, edges, labels: str):
        if n == 1:
            return [1]
        if n == 0:
            return []
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        d = {i: set() for i in range(n)}
        memo = {i: {x: 0 for x in alpha} for i in range(n)}
        for e in edges:
            d[e[0]].add(e[1])
            d[e[1]].add(e[0])

        def dfs(i):
            if visited[i]:
                return False
            visited[i] = True
            memo[i][labels[i]] += 1
            for child in d[i]:
                if dfs(child):
                    for c in alpha:
                        memo[i][c] += memo[child][c]
            return True

        visited = [False] * n
        dfs(0)
        ans = [0] * n
        for i in range(n):
            ans[i] = memo[i][labels[i]]
        return ans


s = Solution()
print(s.countSubTrees(4,
                      [[0, 2], [0, 3], [1, 2]],
                      "aeed"
                      ))
