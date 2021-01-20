class Solution:
    def jump(self, nums) -> int:
        n = len(nums)
        jump = [n] * n
        q = [0]
        jump[0] = 0
        start = 1
        while (q):
            newQ = []
            for i in q:
                for j in range(start, min(i + nums[i] + 1, n)):
                    if j == n - 1:
                        return jump[i] + 1
                    if jump[j] == n:
                        jump[j] = jump[i] + 1
                        newQ.append(j)
            start = min(i + nums[i] + 1, n)
            q = newQ
        return jump[n - 1]


s = Solution()
print(s.jump([2, 3, 1, 1, 4]))
