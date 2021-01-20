class Solution:
    def judgePoint24(self, nums) -> bool:
        eps = 0.001

        def help2(x, y):
            res = [x + y, x * y, x - y, y - x]
            if abs(y) > eps:
                res.append(x / y)
            if abs(x) > eps:
                res.append(y / x)
            return res

        def help3(a, b, c):
            res = []
            for x in help2(b, c):
                res += help2(a, x)
            for x in help2(a, c):
                res += help2(b, x)
            for x in help2(a, b):
                res += help2(c, x)
            return res

        def f2(a, b, c, d):
            res = []
            h2x = help2(a, b)
            h2y = help2(c, d)
            for x in h2x:
                for y in h2y:
                    res += help2(x, y)
            return res

        def f3(a, b, c, d):
            res = []
            h3 = help3(b, c, d)
            for x in h3:
                res += help2(a, x)
            return res

        ans = f2(nums[0], nums[1], nums[2], nums[3])
        ans += f2(nums[0], nums[2], nums[1], nums[3])
        ans += f2(nums[0], nums[3], nums[1], nums[2])
        ans += f3(nums[0], nums[1], nums[2], nums[3])
        ans += f3(nums[1], nums[0], nums[2], nums[3])
        ans += f3(nums[2], nums[0], nums[1], nums[3])
        ans += f3(nums[3], nums[0], nums[1], nums[2])
        for x in ans:
            if abs(x - 24) < eps:
                return True
        return False


s = Solution()
print(s.judgePoint24([4, 1, 8, 7]))
print(s.judgePoint24([1, 5, 9, 1]))
print(s.judgePoint24([1, 2, 1, 2]))
