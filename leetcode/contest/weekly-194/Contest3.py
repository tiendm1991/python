import random
import bisect


class Solution:
    def avoidFlood(self, rains):
        n = len(rains)
        ans = [-1 for i in range(n)]
        zeros = []
        stack = {}
        impossible = False

        def findZero(low, high, _min, _max):
            if low > high or zeros[low] >= _max or zeros[high] < _min:
                return -1
            if zeros[low] >= _min:
                return low
            mid = (low + high) // 2
            if zeros[mid] < _min:
                return findZero(mid + 1, high, _min, _max)
            else:
                return findZero(low, mid, _min, _max)

        for i in range(n):
            if rains[i] == 0:
                zeros.append(i)
                continue
            if rains[i] in stack:
                idx = bisect.bisect(zeros, stack[rains[i]])
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
# print(s.avoidFlood([2, 3, 0, 0, 3, 1, 0, 1, 0, 2, 2]))  # [2, 3, 6, 8]
# print(s.avoidFlood([1,2,0,0,2,1]))
# print(s.avoidFlood([69,0,0,0,69]))
# print(s.avoidFlood([0,1,1]))
print(s.avoidFlood([1,2,0,1,2]))
# print(s.avoidFlood([3,5,4,0,1,0,1,5,2,8,9]))
