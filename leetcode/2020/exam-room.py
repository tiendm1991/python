import bisect


class ExamRoom:

    def __init__(self, N: int):
        self.n = N
        self.a = []

    def seat(self) -> int:
        if not self.a:
            ans = 0
        else:
            ans, _max = 0, self.a[0]
            for i in range(1, len(self.a)):
                if self.a[i] - self.a[i - 1] == 1:
                    continue
                mid = (self.a[i] + self.a[i - 1]) // 2
                if mid - self.a[i - 1] > _max:
                    _max = mid - self.a[i - 1]
                    ans = mid
            if _max < self.n - 1 - self.a[-1]:
                ans = self.n - 1
        bisect.insort(self.a, ans)
        return ans

    def leave(self, p: int) -> None:
        self.a.remove(p)


# Your ExamRoom object will be instantiated and called as such:
obj = ExamRoom(4)
print(obj.seat())
print(obj.seat())
print(obj.seat())
print(obj.seat())
obj.leave(1)
obj.leave(3)
print(obj.seat())
