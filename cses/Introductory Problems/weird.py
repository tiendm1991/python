def f(n):
    result = ""
    while n > 1:
        result += str(n) + " "
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
    return result + "1"


n = int(input())
print(f(n))
