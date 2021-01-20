class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        l = 2 ** (N - 1)

        def biSearch(n, k):
            if k == 1:
                return 0
            elif k == 2:
                return 1
            if k <= n // 2:
                return biSearch(n // 2, k)
            else:
                return 1 - biSearch(n // 2, k - n // 2)

        return biSearch(l, K)
