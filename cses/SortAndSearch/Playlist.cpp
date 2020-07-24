n = int(input())
arr = [int(c) for c in input().split(' ')]
arr.append(arr[-1])
start = 0
ans = 1
d = {arr[0]: 0}
for i in range(1, n+1):
    v = arr[i]
    if v in d:
        ans = max(ans, i - start)
        tmp = start + 1
        if v in d:
            tmp = max(start, d[v]) + 1
        for j in range(start, tmp):
            if arr[j] in d:
                del d[arr[j]]
        start = tmp
    d[v] = i
print(ans)
