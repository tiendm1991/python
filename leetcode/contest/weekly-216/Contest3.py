class Solution:
    def waysToMakeFair(self, nums) -> int:
        n = len(nums)
        if n == 1:
            return 1
        if n == 2:
            return 0

        even, odd = [nums[i] if i % 2 == 0 else 0 for i in range(n)], \
                    [nums[i] if i % 2 == 1 else 0 for i in range(n)]
        sOdd, sEven = 0, 0
        for i in range(n):
            if odd[i] != 0:
                odd[i] += sOdd
                sOdd = odd[i]
            if even[i] != 0:
                even[i] += sEven
                sEven = even[i]
        s = sum(nums)
        ans = 0
        for i in range(n):
            sTmp = s - nums[i]
            if sTmp & 1:
                continue
            if i == 0:
                x = max(odd[-1], odd[-2])
            elif i == n - 1:
                x = max(odd[n - 2], even[n - 2])
            elif i % 2 == 0:
                x = odd[i - 1] + max(even[-1], even[-2]) - even[i]
            else:
                x = even[i - 1] + max(odd[-1], odd[-2]) - odd[i]
            if 2 * x == sTmp:
                ans += 1
        return ans


s = Solution()
print(s.waysToMakeFair([1, 1, 1]))
# print(s.waysToMakeFair([2, 1, 6, 4]))
