# https://leetcode.com/contest/weekly-contest-200/problems/minimum-swaps-to-arrange-a-binary-grid/
class Solution:
    def minSwaps(self, grid) -> int:
        n = len(grid)
        c = {}
        for i in range(n):
            c[i] = 0
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    c[i] += 1
                else:
                    break
        ans = 0
        for i in range(n):
            a = n - 1 - i
            j = i
            while j < n and c[j] < a:
                j += 1
            if j == n:
                return -1
            k = j
            while k > i:
                grid[k], grid[k - 1] = grid[k - 1], grid[k]
                c[k], c[k - 1] = c[k - 1], c[k]
                k -= 1
                ans += 1
        return ans


s = Solution()
print(s.minSwaps([[0, 0, 1], [1, 1, 0], [1, 0, 0]]))
print(s.minSwaps([[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]]))
print(s.minSwaps([[1, 0, 0], [1, 1, 0], [1, 1, 1]]))
