def minAndMaxValueOfExp(s):
    start, i = 0, 0
    num = []
    op = []
    while (i < len(s)):
        if s[i] == '+' or s[i] == '*':
            op.append(s[i])
            num.append(int(s[start:i]))
            start = i + 1
        i += 1
    num.append(int(s[start:]))
    n = len(num)
    dpMin = [[999 for i in range(n)] for j in range(n)]
    dpMax = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        dpMin[i][i] = num[i]
        dpMax[i][i] = num[i]
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            if j - i == 1:
                dpMin[i][j] = calculate(num[i], num[j], op[i])
                dpMax[i][j] = calculate(num[i], num[j], op[i])
                continue
            for k in range(i + 1, j):
                dpMin[i][j] = min(dpMin[i][j], calculate(dpMin[i][k - 1], dpMin[k][j], op[k - 1]),
                                  calculate(dpMin[i][k], dpMin[k + 1][j], op[k]))
                dpMax[i][j] = max(dpMax[i][j], calculate(dpMax[i][k - 1], dpMax[k][j], op[k - 1]),
                                  calculate(dpMax[i][k], dpMax[k + 1][j], op[k]))
    return [dpMin[0][n - 1], dpMax[0][n - 1]]


def calculate(x, y, o):
    if o == '+':
        return x + y
    elif o == '*':
        return x * y
    else:
        return x


print(minAndMaxValueOfExp('1+2*3+4*5'))
