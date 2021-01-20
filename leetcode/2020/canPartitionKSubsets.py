class Solution:
    def canPartitionKSubsets(self, nums, k: int) -> bool:
        s = sum(nums)
        n = len(nums)
        if s % k != 0:
            return False
        t = s // k
        a = [0] * k
        visited = [False] * n

        def backtrack(i, start):
            if i == k - 1:
                return True
            for j in range(start, n):
                if visited[j] or a[i] + nums[j] > t:
                    continue
                a[i] += nums[j]
                visited[j] = True
                if a[i] == t:
                    check = backtrack(i + 1, 0)
                else:
                    check = backtrack(i, j + 1)
                if check:
                    return True
                a[i] -= nums[j]
                visited[j] = False
            return False

        return backtrack(0, 0)


s = Solution()
print(s.canPartitionKSubsets([10, 10, 10, 7, 7, 7, 7, 7, 7, 6, 6, 6], 3))
