def nearestGreater(a):
    MAX_INTEGER = 10**9
    n = len(a)
    rightGreater = [MAX_INTEGER] * n
    leftGreater = [-MAX_INTEGER] * n
    result = [-1] * n
    stack = []
    for i in range(n):
        while stack and a[stack[-1]] < a[i]:
            rightGreater[stack.pop()] = i
        stack.append(i)
    stack = []
    for i in range(n-1, -1, -1):
        while stack and a[stack[-1]] < a[i]:
            leftGreater[stack.pop()] = i
        stack.append(i)
    for i in range(n):
        if leftGreater[i] != -MAX_INTEGER or rightGreater[i] != MAX_INTEGER:
            if i - leftGreater[i] <= rightGreater[i] - i:
                result[i] = leftGreater[i]
            else:
                result[i] = rightGreater[i]
    return result
print(nearestGreater([7, 4, 7, 2, 7, 6]))