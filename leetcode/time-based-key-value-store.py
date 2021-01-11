import bisect


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = [(timestamp, value)]
        else:
            bisect.insort(self.d[key], (timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d or self.d[key][0][0] > timestamp:
            return ""
        a = self.d[key]
        i = bisect.bisect_left(a, (timestamp + 1, ""))
        return a[i - 1][1]


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("foo", "bar", 1)
print(obj.get("foo", 1))
print(obj.get("foo", 3))
obj.set("foo", "bar2", 4)
print(obj.get("foo", 4))
print(obj.get("foo", 5))
