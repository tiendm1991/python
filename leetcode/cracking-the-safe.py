class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        init = '0' * n
        visited = {init}
        target = k ** n

        def bactrack(cur, x):
            if x == target:
                return cur
            last = '' if n == 1 else cur[-(n - 1):]
            for i in range(k):
                check = last + str(i)
                if check not in visited:
                    visited.add(check)
                    ans = bactrack(cur + str(i), x + 1)
                    if ans:
                        return ans
                    visited.remove(check)
            return None

        return bactrack(init, 1)


s = Solution()
print(s.crackSafe(1, 2))
