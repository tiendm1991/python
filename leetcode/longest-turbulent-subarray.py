class Solution:
    def maxTurbulenceSize(self, arr) -> int:
        arr.append(arr[-1])
        n = len(arr)
        if n == 1:
            return 1
        res = 1
        start = 1
        while start < n and arr[start] == arr[start - 1]:
            start += 1
        if start == n:
            return 1
        for i in range(start + 1, n):
            if (arr[i] - arr[i - 1]) * (arr[i - 1] - arr[i - 2]) >= 0:
                res = max(res, i - start + 1)
                if arr[i] - arr[i - 1] == 0:
                    start = i + 1
                else:
                    start = i
        return res


s = Solution()
print(s.maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]))
print(s.maxTurbulenceSize([4, 8, 12, 16]))
