class Solution:
    def possibleBipartition(self, N: int, dislikes) -> bool:
        a = [[0 if i == 0 or j == 0 else 1 for i in range(N+1)] for j in range(N+1)]
        for p in dislikes:
            a[p[0]][p[1]] = 0
            a[p[1]][p[0]] = 0
        count = 0
        def dfs(i):
            a[i][i] = 0
            for j in range(1, N+1):
                if a[j][j] == 1 and a[i][j] == 1 and j > i:
                    dfs(j)
        for i in range(1, N+1):
            if a[i][i] != 0:
                count += 1
                dfs(i)
        return count <= 2
s = Solution()
print(s.possibleBipartition(4, [[1,2],[2,3],[3,4]]))