class Solution:
    def numSubarraysWithSum(self, a, s: int) -> int:
        def calculateSumZero(arr):
            arr += [1]
            start = -1
            res = 0
            for i in range(len(arr)):
                if arr[i] == 0 and start == -1:
                    start = i
                elif arr[i] == 1:
                    if start != -1:
                        l = i - start
                        res += l * (l + 1) // 2
                    start = -1
            return res

        n = len(a)
        res = 0
        if s == 0:
            return calculateSumZero(a)
        b = [-1] + [i for i in range(n) if a[i] == 1] + [n]
        i, j = 1, s
        while j < len(b) - 1:
            res += (b[i] - b[i - 1]) * (b[j + 1] - b[j])
            i += 1
            j += 1
        return res


s = Solution()
print(s.numSubarraysWithSum([0, 0, 0, 0, 0], 0))
print(s.numSubarraysWithSum([1, 0, 1, 0, 1], 2))
print(s.numSubarraysWithSum([0, 1, 0, 1, 0, 1], 2))
print(s.numSubarraysWithSum([1, 0, 1, 0, 1, 0, 1], 2))
