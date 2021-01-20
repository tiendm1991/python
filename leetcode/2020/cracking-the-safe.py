class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        init = '0' * n
        visited = {init}
        target = k ** n

        def backtrack(cur, count):
            if count == target:
                return cur
            last = '' if n == 1 else cur[-(n - 1):]
            for i in range(k):
                check = last + str(i)
                if check not in visited:
                    visited.add(check)
                    ans = backtrack(cur + str(i), count + 1)
                    if ans:
                        return ans
                    visited.remove(check)
            return None

        return backtrack(init, 1)


s = Solution()
print(s.crackSafe(1, 2))
