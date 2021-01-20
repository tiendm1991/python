class Solution:
    def minSwap(self, a, b) -> int:
        n = len(a)
        if n == 1:
            return True
        swap, notSwap = [n] * n, [n] * n
        swap[0], notSwap[0] = 1, 0
        for i in range(1, n):
            if a[i] > a[i - 1] and b[i] > b[i - 1]:
                notSwap[i] = notSwap[i - 1]
                swap[i] = 1 + swap[i - 1]
            if a[i] > b[i - 1] and b[i] > a[i - 1]:
                notSwap[i] = min(notSwap[i], swap[i - 1])
                swap[i] = min(swap[i], 1 + notSwap[i - 1])
        return min(swap[n - 1], notSwap[n - 1])


s = Solution()
print(s.minSwap([0, 4, 4, 5, 9],
                [0, 1, 6, 8, 10]))
print(s.minSwap([0, 7, 8, 10, 10, 11],
                [4, 4, 5, 7, 11, 14]))
print(s.minSwap([1, 3, 5, 4, 6], [1, 2, 3, 7, 8]))
print(s.minSwap([4, 3, 7], [1, 2, 8]))
