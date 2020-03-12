import functools
from datetime import datetime, time
import math
import bisect
import random
import collections



class Solution:
    def circularArrayLoop(self, nums) -> bool:
        n = len(nums)
        visited = [False] * n
        for i in range(n):
            if visited[i]:
                continue
            cur = i
            track = [i]
            visited[i] = True
            forward = nums[i] // abs(nums[i])
            while True:
                cur = (cur + nums[cur]) % n
                if nums[cur] * forward < 0:
                    break
                elif nums[cur] % n == 0:
                    visited[cur] = True
                    break
                elif cur in track:
                    if (cur == i and len(track) > 1) or len(track) > 2:
                        return True
                    else:
                        visited[cur] = True
                        break
                elif visited[cur]:
                    break
                else:
                    track.append(cur)
                    visited[cur] = True
        return False


    def circularArrayLoop2(self, nums) -> bool:
        n = len(nums)
        visited = [False] * n
        for i in range(n):
            if visited[i]:
                continue
            cur = i
            track = []
            forward = nums[i] // abs(nums[i])
            while nums[cur] * forward >= 0:
                if nums[cur] % n == 0:
                    visited[cur] = True
                    break
                elif cur in track:
                    if (cur == i and len(track) > 1) or len(track) > 2:
                        return True
                    else:
                        visited[cur] = True
                        break
                elif visited[cur]:
                    break
                else:
                    track.append(cur)
                    visited[cur] = True
                visited[cur] = True
                cur = (cur + nums[cur]) % n
        return False


s = Solution()
startTime = datetime.now()
print(s.circularArrayLoop([-1,2,1,2]))
print(datetime.now() - startTime)

