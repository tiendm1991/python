def pow(x, n):
    if n == 0:
        return 1
    tmp = pow(x, n//2)
    if n % 2 == 0:
        return tmp * tmp
    return x * tmp * tmp


print(pow(3, 5))

