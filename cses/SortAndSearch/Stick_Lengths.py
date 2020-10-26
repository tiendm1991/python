n = int(input())
a = [int(c) for c in input().split(' ')]
a.sort()
avg = a[n // 2]
ans = 0
for x in a:
    ans += abs(x - avg)
print(ans)
