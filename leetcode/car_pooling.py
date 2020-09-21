class Solution:
    def carPooling(self, trips, capacity: int) -> bool:
        c = 0
        a = []
        for t in trips:
            a.append([t[1], 1, t[0]])
            a.append([t[2], -1, t[0]])
        a = sorted(a)
        for t in a:
            c += t[2] * t[1]
            if c > capacity:
                return False
        return True


s = Solution()
print(s.carPooling([[2, 1, 5], [3, 3, 7]], 4))
print(s.carPooling([[2, 1, 5], [3, 3, 7]], 5))
