import heapq


class FreqStackUsingHeap:

    def __init__(self):
        self.a = {}
        self.h = []
        self.i = 0

    def push(self, x: int) -> None:
        if x not in self.a:
            self.a[x] = [self.i]
        else:
            self.a[x].append(self.i)
        heapq.heappush(self.h, [-len(self.a[x]), -self.i, x])
        self.i += 1

    def pop(self) -> int:
        t = heapq.heappop(self.h)
        self.a[t[2]].pop()
        return t[2]


class FreqStack:

    def __init__(self):
        self.countElement = {}
        self.count = {}
        self.freqStack = []

    def push(self, x: int) -> None:
        self.count[x] = self.count.get(x, 0) + 1
        if self.count[x] not in self.countElement:
            self.countElement[self.count[x]] = []
        self.countElement[self.count[x]].append(x)
        if not self.freqStack or self.count[x] > self.freqStack[-1]:
            self.freqStack.append(self.count[x])

    def pop(self) -> int:
        freq = self.freqStack[-1]
        x = self.countElement[freq].pop()
        self.count[x] -= 1
        if len(self.countElement[freq]) == 0:
            self.freqStack.pop()
        return x


# Your FreqStack object will be instantiated and called as such:
obj = FreqStack()
obj.push(5)
obj.push(7)
obj.push(5)
obj.push(7)
obj.push(4)
obj.push(5)
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
