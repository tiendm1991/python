class Solution:
    def findKthPositive(self, arr, k: int) -> int:
        n = len(arr)
        if arr[-1] - n < k:
            # arr[-1] + k - (arr[-1] - n)
            return k + n
        if arr[0] > k:
            return k
        k -= arr[0] - 1
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            left_missing = arr[m] - arr[l] - (m - l)
            if left_missing >= k:
                r = m
            else:
                k -= left_missing
                if arr[m] + k < arr[m + 1]:
                    return arr[m] + k
                else:
                    l = m + 1
                    k -= arr[m + 1] - arr[m] - 1
        return 0


s = Solution()
print(s.findKthPositive([2, 3, 4, 7, 11], 5))
print(s.findKthPositive([1, 2, 3, 4], 2))
