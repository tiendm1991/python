class Solution:

    def minMoves_slow(self, nums, limit: int) -> int:
        n = len(nums)
        if n == 2:
            return 0
        d = {}
        for i in range(n // 2):
            x = nums[i] + nums[n - 1 - i]
            d[x] = d.get(x, 0) + 1
        s = []
        for k in d:
            if not s or d[k] > d[s[0]]:
                s = [k]
            elif d[k] == d[s[0]]:
                s.append(k)
        res = n
        for target in s:
            tmp = 0
            for i in range(n // 2):
                if nums[i] + nums[n - 1 - i] > target:
                    if min(nums[i], nums[n - 1 - i]) + 1 > target:
                        tmp += 2
                    else:
                        tmp += 1
                elif nums[i] + nums[n - 1 - i] < target:
                    if max(nums[i], nums[n - 1 - i]) + limit < target:
                        tmp += 2
                    else:
                        tmp += 1
            res = min(res, tmp)
        return res

    def minMoves(self, nums, limit: int) -> int:
        n = len(nums)
        if n == 2:
            return 0
        d = {i: 0 for i in range(2 * limit + 2)}
        for i in range(n // 2):
            x, y = nums[i], nums[n - 1 - i]
            # init
            d[2] += 2
            # calculate with each target
            d[min(x, y) + 1] -= 1
            d[x + y] -= 1
            d[x + y + 1] += 1
            d[max(x, y) + limit + 1] += 1

        res = n
        for i in range(2, 2 * limit + 1):
            d[i] += d[i - 1]
            res = min(res, d[i])
        return res


s = Solution()
print(s.minMoves([1, 2, 2, 1], 2))
print(s.minMoves([1, 1, 1, 2, 2, 3], 4))
print(s.minMoves(
    [16, 34, 41, 55, 41, 32, 13, 43, 25, 34, 57, 8, 32, 25, 55, 48, 57, 19, 47, 54, 58, 15, 49, 52, 45, 32, 10, 26, 19,
     53, 58, 37, 3, 32, 21, 11, 7, 7], 60))
print(s.minMoves([1, 2, 4, 3], 4))
