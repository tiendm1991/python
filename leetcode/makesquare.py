import functools
from datetime import datetime, time
import math
import bisect
import random
import collections

from testcases.cebu import Util
from testcases.cebu.Util import ListNode, TreeNode


class Solution:
    def makesquare(self, nums) -> bool:
        n = len(nums)
        s = sum(nums)
        if s == 0 or s % 4 != 0:
            return False
        s //= 4
        m = max(nums)
        if m > s:
            return False

        def backtrack2(a, idx):
            if idx == n:
                return True
            for i in range(4):
                if a[i] + nums[idx] > s:
                    continue
                a[i] += nums[idx]
                if backtrack2(a, idx+1):
                    return True
                a[i] -= nums[idx]
            return False

        nums = sorted(nums, reverse=True)
        def backtrack(a, visited, idx):
            if idx == 3:
                return True
            for i in range(n):
                if visited[i]:
                    continue
                if a[idx] + nums[i] > s:
                    continue
                elif a[idx] + nums[i] <= s:
                    a[idx] += nums[i]
                    visited[i] = True
                    tmp = idx + 1 if a[idx] == s else idx
                    if backtrack(a, visited, tmp):
                        return True
                    a[idx] -= nums[i]
                    visited[i] = False
            return False

        arr = [0] * 4
        visited = [False] * n
        if nums[-1] < n:
            return backtrack2(arr, 0)
        else:
            return backtrack(arr, visited, 0)


s = Solution()
startTime = datetime.now()
print(s.makesquare([5,5,5,5,16,4,4,4,4,4,3,3,3,3,4]))
print(datetime.now() - startTime)

