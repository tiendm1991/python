class Solution:
    def constructDistancedSequence(self, n: int):
        choose = set(range(1, n + 1))

        def backtrack(a, i):
            if i == 2 * n - 1:
                return a
            if a[i] != 0:
                return backtrack(a, i + 1)
            for x in range(n, 0, -1):
                if x not in choose:
                    continue
                if x == 1:
                    choose.remove(x)
                    a[i] = 1
                    res = backtrack(a, i + 1)
                    if res:
                        return res
                    a[i] = 0
                    choose.add(x)
                if i + x < 2 * n - 1 and a[i + x] == 0:
                    choose.remove(x)
                    a[i] = x
                    a[i + x] = x
                    res = backtrack(a, i + 1)
                    if res:
                        return res
                    a[i] = 0
                    a[i + x] = 0
                    choose.add(x)
            return None

        return backtrack([0] * (2 * n - 1), 0)


s = Solution()
print(s.constructDistancedSequence(3))
print(s.constructDistancedSequence(5))
print(s.constructDistancedSequence(10))
