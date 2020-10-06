class Solution:
    def maxChunksToSorted(self, arr) -> int:
        n = len(arr)
        ans = 1
        m = [0] * n
        m[0] = arr[0]
        for i in range(1, n):
            m[i] = max(m[i - 1], arr[i])
        mi = arr[-1]
        for j in range(n - 2, -1, -1):
            if m[j] < mi:
                ans += 1
            mi = min(mi, arr[j])
        return ans


s = Solution()
print(s.maxChunksToSorted([1, 0, 3, 2, 4]))
