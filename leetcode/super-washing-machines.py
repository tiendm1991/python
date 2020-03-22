from datetime import datetime


class Solution:
    def findMinMoves(self, machines) -> int:
        n = len(machines)
        if n == 1:
            return 0
        s = sum(machines)
        n = len(machines)
        if s % n != 0:
            return -1
        avg = s // n
        move = [0] * n
        for i in range(n - 1):
            x = machines[i]
            if x == avg:
                continue
            elif x < avg:
                machines[i + 1] -= (avg - x)
                move[i + 1] += (avg - x)
            else:
                machines[i + 1] += (x - avg)
                move[i] += x - avg
            machines[i] = avg
        return max(move)


s = Solution()
startTime = datetime.now()
print(s.findMinMoves([4, 0, 0, 4]))
print(datetime.now() - startTime)
