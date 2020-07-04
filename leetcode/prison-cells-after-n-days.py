class Solution:
    def prisonAfterNDays(self, cells, N: int):
        memo = []
        count = 1
        idx = -1
        while count <= N:
            count += 1
            cur = [0] * 8
            prev = cells if len(memo) == 0 else memo[-1]
            for i in range(1, 7):
                if prev[i - 1] == prev[i + 1]:
                    cur[i] = 1
            if cur in memo:
                idx = memo.index(cur)
                break
            else:
                memo.append(cur)
        if idx == -1:
            return memo[-1]
        return memo[idx + (N - 1 - idx) % (len(memo) - idx)]


s = Solution()
print(s.prisonAfterNDays([0,1,0,1,1,0,0,1], 7))
print(s.prisonAfterNDays([1,1,0,1,1,0,1,1], 6))
print(s.prisonAfterNDays([0,0,1,1,1,1,0,0], 8))
print(s.prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000))
