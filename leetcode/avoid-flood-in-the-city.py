import random
from sortedcontainers import SortedSet

class Solution:
    def avoidFlood(self, rains):
        n = len(rains)
        ans = [-1 for i in range(n)]
        zeros = SortedSet([])
        stack = {}
        impossible = False
        for i in range(n):
            if rains[i] == 0:
                zeros.add(i)
                continue
            if rains[i] in stack:
                idx = zeros.bisect(stack[rains[i]])
                idxZero = None
                if idx < len(zeros) and zeros[idx] > stack[rains[i]]:
                    idxZero = zeros.pop(idx)
                if idxZero is None:
                    impossible = True
                    break
                ans[idxZero] = rains[i]
            stack[rains[i]] = i
        if impossible:
            return []
        stack = set()
        for i in range(n):
            if rains[i] > 0:
                stack.add(rains[i])
            elif ans[i] == -1:
                if stack:
                    ans[i] = stack.pop()
                else:
                    ans[i] = random.randrange(1, n)
            else:
                stack.remove(ans[i])
        # for i in zeros:
        #     ans[i] = random.randrange(1, n)
        return ans


s = Solution()
# print(s.avoidFlood([1, 1, 0, 0]))
print(s.avoidFlood([2,3,0,0,3,1,0,1,0,2,2])) #[2, 3, 6, 8]
# print(s.avoidFlood([1,2,0,0,2,1]))
# print(s.avoidFlood([69,0,0,0,69]))
# print(s.avoidFlood([0,1,1]))
# print(s.avoidFlood([1,2,0,1,2]))
# print(s.avoidFlood([3,5,4,0,1,0,1,5,2,8,9]))
