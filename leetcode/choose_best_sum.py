def choose_best_sum1(t, k, ls):
    n = len(ls)
    _max = [-1]

    def backtrack(_max, ls, visited, count, s):
        if count == k:
            _max[0] = max(_max[0], s)
            return
        for i, x in enumerate(ls):
            if not visited[i] and s + x <= t:
                visited[i] = True
                backtrack(_max, ls, visited, count + 1, s + x)
                visited[i] = False

    visited = [False] * n
    backtrack(_max, ls, visited, 0, 0)
    return _max[0] if _max[0] != -1 else None


def choose_best_sum2(t, k, ls):
    n = len(ls)
    if k > n:
        return None
    dp = [[[-1 for j in range(t + 1)] for i in range(k + 1)] for _ in range(n)]

    def recurse(t, k, idx):
        if k == 0:
            return 0
        if idx == -1:
            return -1
        if dp[idx][k][t] != -1:
            return dp[idx][k][t]
        not_choose = recurse(t, k, idx - 1)
        choose = -1
        if ls[idx] <= t:
            x = recurse(t - ls[idx], k - 1, idx - 1)
            if x > -1:
                choose = ls[idx] + x
        _max = max(choose, not_choose)
        dp[idx][k][t] = _max
        return _max

    result = recurse(t, k, n - 1)
    return result if result > 0 else None


def choose_best_sum(t, k, ls):
    n = len(ls)
    if k > n:
        return None
    dp = [[[0 if b == 0 else -1 for j in range(t + 1)] for b in range(k + 1)] for a in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            for l in range(1, t + 1):
                not_choose = dp[i - 1][j][l]
                choose = -1
                if l >= ls[i - 1] and dp[i - 1][j - 1][l - ls[i - 1]] != -1:
                    choose = ls[i - 1] + dp[i - 1][j - 1][l - ls[i - 1]]
                dp[i][j][l] = max(choose, not_choose)
    return dp[n][k][t] if dp[n][k][t] > -1 else None


# print(choose_best_sum(6, 2, [1, 2, 3, 5]))
print(choose_best_sum(174, 3, [50, 55, 57, 58, 60]))
# print(choose_best_sum(430, 8, [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]))
