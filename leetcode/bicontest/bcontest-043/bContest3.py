class Solution:
    def constructDistancedSequence(self, n: int):
        d = {i: 2 for i in range(2, n + 1)}
        d[1] = 1

        def backtrack(a, i):
            if i == 2 * n - 1:
                return a
            if a[i] != 0:
                return backtrack(a, i + 1)
            for x in range(n, 0, -1):
                if x == 1:
                    if d[x] == 1:
                        d[x] -= 1
                        a[i] = 1
                        res = backtrack(a, i + 1)
                        if res:
                            return res
                        a[i] = 0
                        d[x] += 1
                    else:
                        return None
                if d[x] == 2 and i + x < 2 * n - 1 and a[i + x] == 0:
                    d[x] -= 2
                    a[i] = x
                    a[i + x] = x
                    res = backtrack(a, i + 1)
                    if res:
                        return res
                    a[i] = 0
                    a[i + x] = 0
                    d[x] += 2
            return

        return backtrack([0] * (2 * n - 1), 0)


s = Solution()
print(s.constructDistancedSequence(3))
print(s.constructDistancedSequence(5))
print(s.constructDistancedSequence(10))
