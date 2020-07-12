def valid(i, j):
    return 0 <= i < 7 and 0 <= j < 7 and not visited[i][j]


def dfs(i, j, step, m):
    if i == 6 and j == 0:
        if step == 48:
            result[0] += 1
        return

    if m == 'L' and (j == 0 or visited[i][j - 1]) and 0 < i < 6 and not visited[i - 1][j] and not visited[i + 1][j]:
        return
    if m == 'R' and (j == 6 or visited[i][j + 1]) and 0 < i < 6 and not visited[i - 1][j] and not visited[i + 1][j]:
        return
    if m == 'U' and (i == 0 or visited[i - 1][j]) and 0 < j < 6 and not visited[i][j - 1] and not visited[i][j + 1]:
        return
    if m == 'D' and (i == 6 or visited[i + 1][j]) and 0 < j < 6 and not visited[i][j - 1] and not visited[i][j + 1]:
        return

    visited[i][j] = True
    ch = a[step]
    if ch == '?' or ch == 'D':
        if valid(i + 1, j):
            dfs(i + 1, j, step + 1, m)
    if ch == '?' or ch == 'U':
        if valid(i - 1, j):
            dfs(i - 1, j, step + 1, m)
    if ch == '?' or ch == 'L':
        if valid(i, j - 1):
            dfs(i, j - 1, step + 1, m)
    if ch == '?' or ch == 'R':
        if valid(i, j + 1):
            dfs(i, j + 1, step + 1, m)
    visited[i][j] = False
    return


result = [0]
s = input()
a = [c for c in s]
visited = [[False for j in range(7)] for i in range(7)]

# Solve
dfs(0, 0, 0, '.')
print(result[0])
