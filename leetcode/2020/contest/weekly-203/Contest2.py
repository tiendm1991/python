class Solution:
    def getWinner(self, arr, k: int) -> int:
        ans = max(arr[0], arr[1])
        c = 1
        for i in range(2, len(arr)):
            if c == k:
                return ans
            if ans > arr[i]:
                c += 1
            else:
                ans = arr[i]
                c = 1
        return ans


s = Solution()
print(s.findLHS([3, 3, -3, 2, 2, 3, 3]))
