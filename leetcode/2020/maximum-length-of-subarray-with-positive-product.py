class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        nums = [x // abs(x) if x != 0 else 0 for x in nums]
        nums.append(0)
        n = len(nums)

        def help(a):
            if len(a) == 0:
                return 0
            N = len(a)
            pre = [1] * (N + 1)
            p1, p2, n1, n2 = -1, -1, -1, -1
            for i in range(1, N + 1):
                pre[i] = pre[i - 1] * a[i - 1]
            for i in range(N + 1):
                if pre[i] == 1:
                    if p1 == -1:
                        p1 = i
                    else:
                        p2 = i
                else:
                    if n1 == -1:
                        n1 = i
                    else:
                        n2 = i
            return max(p2 - p1, n2 - n1)

        start = 0
        ans = 0
        for i in range(n):
            if nums[i] == 0:
                ans = max(ans, help(nums[start: i]))
                start = i + 1
        return ans
