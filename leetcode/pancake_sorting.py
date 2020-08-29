class Solution:
    def pancakeSort(self, a):
        n = len(a)
        ans = []
        for x in range(n, 1, -1):
            i = a.index(x)
            if i == x - 1:
                continue
            elif i == 0:
                ans.append(x)
                a[:x] = reversed(a[:x])
            else:
                ans.append(i + 1)
                a[:i + 1] = reversed(a[:i + 1])
                ans.append(x)
                a[:x] = reversed(a[:x])
        return ans


s = Solution()
print(s.pancakeSort([3, 2, 4, 1]))
