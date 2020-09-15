class Solution:
    def constructArray(self, n: int, k: int):
        if k == 1:
            return list(range(1, n + 1))
        ans = []
        i, a, b = 0, 1, n
        while k > 1:
            if i % 2 == 0:
                ans.append(a)
                a += 1
            else:
                ans.append(b)
                b -= 1
            i += 1
            k -= 1
        if i % 2 == 0:
            return ans + list(range(a, b + 1))
        else:
            return ans + list(range(b, a - 1, -1))


s = Solution()
print(s.constructArray(6, 3))
print(s.constructArray(6, 4))
