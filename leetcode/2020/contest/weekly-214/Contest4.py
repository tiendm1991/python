import bisect


class Solution:
    def createSortedArray_bisearch(self, instructions) -> int:
        mod = 10 ** 9 + 7
        nums = []
        n = len(instructions)
        if n < 2:
            return 0

        def insert(x):
            left, right = bisect.bisect_left(nums, x), len(nums) - bisect.bisect_right(nums, x)
            bisect.insort(nums, x)
            return min(left, right)

        ans = 0
        for x in instructions:
            if not nums:
                nums = [x]
                continue
            ans = (ans + insert(x)) % mod
        return ans

    def createSortedArray_fenwick(self, instructions) -> int:
        mod = 10 ** 9 + 7
        n = max(instructions)
        a = [0] * (n + 1)

        def get(x):
            res = 0
            while x > 0:
                res += a[x]
                x -= x & -x
            return res

        def update(x):
            while x <= n:
                a[x] += 1
                x += x & -x

        ans = 0
        for i, v in enumerate(instructions):
            ans += min(get(v - 1), i - get(v))
            update(v)
        return ans % mod


s = Solution()
print(s.createSortedArray_fenwick([1, 3, 3, 3, 2, 4, 2, 1, 2]))
print(s.createSortedArray_fenwick([1, 2, 3, 6, 5, 4]))
print(s.createSortedArray_fenwick([1, 5, 6, 2]))
