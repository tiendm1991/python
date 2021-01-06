class Solution:
    def numsSameConsecDiff(self, n: int, k: int):
        q = set([str(x) for x in range(1, 10)])
        length = 1
        while q:
            if length == n:
                return list(q)
            newQ = set()
            for x in q:
                last = int(x[-1])
                if last - k >= 0:
                    newX = x + str(last - k)
                    if newX not in newQ:
                        newQ.add(newX)
                if last + k < 10:
                    newX = x + str(last + k)
                    if newX not in newQ:
                        newQ.add(newX)
            q = newQ
            length += 1
        return []


s = Solution()
print(s.numsSameConsecDiff(3, 7))
print(s.numsSameConsecDiff(2, 1))
