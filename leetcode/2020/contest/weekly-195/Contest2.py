class Solution:
    def canArrange(self, arr, k: int) -> bool:
        d = {i: 0 for i in range(k)}
        for x in arr:
            d[x % k] += 1
        for i in range(k):
            if i != 0 and i != k - i and d[i] != d[k - i]:
                return False
            if (i == 0 or i == k - i) and d[i] % 2 != 0:
                return False
        return True


s = Solution()
print(s.canArrange([-1, 1, -2, 2, -3, 3, -4, 4], 3))
