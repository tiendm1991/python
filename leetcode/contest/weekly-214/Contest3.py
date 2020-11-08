class Solution:
    def maxProfit(self, a, b: int) -> int:
        mod = 10 ** 9 + 7
        ans = 0
        a.sort()
        a = [0] + a
        n = len(a)
        i = n - 1
        while i > 0 and b > 0:
            if (a[i] - a[i - 1]) * (n - i) <= b:
                ans = (ans + (n - i) * (a[i] + (a[i - 1] + 1)) * (a[i] - a[i - 1]) // 2) % mod
                b -= (a[i] - a[i - 1]) * (n - i)
            else:
                h = b // (n - i)
                ans = ans + ((n - i) * (a[i] + a[i] - h + 1) * h // 2) % mod
                b %= (n - i)
                ans = (ans + b * (a[i] - h)) % mod
                break
            i -= 1
        return ans


s = Solution()
print(s.maxProfit([2, 5], 4))
print(s.maxProfit([3, 5], 6))
print(s.maxProfit([1000000000], 1000000000))
