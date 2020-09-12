import heapq


class Solution:
    def smallestRange(self, nums):
        q = []
        _min, _max = 0, 0
        ans = [0, 0]
        for i, a in enumerate(nums):
            _min = min(_min, a[0])
            _max = max(_max, a[0])
            ans[0] = _min
            ans[1] = max(ans[1], a[-1])
            heapq.heappush(q, (a[0], i, 0))
        while q:
            _min, i, j = heapq.heappop(q)
            if _max - _min < ans[1] - ans[0]:
                ans[0] = _min
                ans[1] = _max
            j += 1
            if j == len(nums[i]):
                return ans
            _max = max(_max, nums[i][j])
            heapq.heappush(q, (nums[i][j], i, j))
        return ans


s = Solution()
print(s.smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))
