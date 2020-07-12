def valid(i, j):
    return 0 <= i < 7 and 0 <= j < 7 and not visited[i][j]

def dfs(i, j, step):
    if i == 6 and j == 0:
        if step == 48:
            result[0] += 1
        return
    if a[step] != '?':
        iNext, jNext = i + d[a[step]][0], j + d[a[step]][1]
        if valid(iNext, jNext):
            visited[iNext][jNext] = True
            dfs(iNext, jNext, step+1)
            visited[iNext][jNext] = False
    else:
        for direct in d.values():
            iNext, jNext = i + direct[0], j + direct[1]
            if valid(iNext, jNext):
                visited[iNext][jNext] = True
                dfs(iNext, jNext, step + 1)
                visited[iNext][jNext] = False
    return


result = [0]
s = input()
a = [c for c in s]
visited = [[False for j in range(7)] for i in range(7)]
d = {'D': (1, 0), 'U': (-1, 0), 'L': (0, -1), 'R': (0, 1)}

# Solve
visited[0][0] = True
dfs(0, 0, 0)
print(result[0])
