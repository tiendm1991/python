import math
class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) > 0:
            return self.stack.pop()
        return None

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val

s = CustomStack(3)
s.push(1)
s.push(2)
print(s.pop())
s.push(2)
s.push(3)
s.push(4)
s.increment(5, 100)
s.increment(2, 100)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())