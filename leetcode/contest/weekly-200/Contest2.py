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
print(s.getWinner([1, 11, 22, 33, 44, 55, 66, 77, 88, 99], 1000000000))
