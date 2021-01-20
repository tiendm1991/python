class Solution:
    def asteroidCollision(self, asteroids):
        ans = []
        for x in asteroids:
            if not ans:
                ans.append(x)
                continue
            if x < 0:
                while ans and 0 < ans[-1] < -x:
                    ans.pop()
                if ans:
                    if ans[-1] == -x:
                        ans.pop()
                    elif ans[-1] < 0:
                        ans.append(x)
                else:
                    ans.append(x)
            else:
                ans.append(x)
        return ans


s = Solution()
print(s.asteroidCollision([-2, -1, 1, 2]))
