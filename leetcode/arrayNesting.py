from  datetime import datetime
import collections

class Solution:
    def arrayNesting(self, nums) -> int:
        n = len(nums)
        if n < 2:
            return n
        def dfs(visited, idx):
            if visited[idx]:
                return 0
            visited[idx] = True
            return 1 + dfs(visited, nums[idx])
        visited = [False] * n
        _max = 0
        for i in range(n):
            _max = max(_max, dfs(visited, i))
        return _max

s = Solution()
startTime = datetime.now()
print(s.arrayNesting([5,4,0,3,1,6,2]))
print(datetime.now() - startTime)