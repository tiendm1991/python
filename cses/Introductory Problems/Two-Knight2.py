i = int(input())
for n in range(1, i + 1):
    x = n ** 2
    total = x * (x - 1) // 2
    print(total - 4 * (n - 1) * (n - 2))

# Explain
# total: total way to choose 2 cell from board (n * n) * (n * n - 1) // 2 (2Cn)
# from 0 -> n-2, each column has 2 + 3 + (n-4) * 4 + 2 + 3 way to choose 2 knight attack each other
# => has (n-2)(4n - 16 + 10) = (n-2)(4n-6)  #(1)
# => at column n-1 => has 1 + 1 + (n-4) * 2 + 1 + 1 way to choose 2 knight attack each other
# => has 2n - 4 = 2(n-2) #(2)
# at column n has 0 way to choose 2 knight attack each other #(3)
# from (1), (2), (3) => has (n-2)(4n-4) = 4(n-1)(n-2) way to choose 2 knight attack each other
# => result = total - 4 * (n-1) * (n-2)
