class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        a = sorted(zip(position, speed))
        n = len(a)
        t = [(target - a[i][0]) / a[i][1] for i in range(n)]
        ans = 0
        cur = 0
        for x in t[::-1]:
            if x > cur:
                cur = x
                ans += 1
        return ans


s = Solution()
print(s.carFleet(10,
                 [4, 0, 2],
                 [1, 2, 3]))
print(s.carFleet(12,
                 [0, 5, 8, 8, 10],
                 [1, 4, 2, 4, 2]))
