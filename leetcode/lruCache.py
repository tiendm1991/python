class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(None, None)
        self.last = Node(None, None)
        self.head.next = self.last
        self.last.prev = self.head
        self.map = {}
        self.count = 0

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        headOld = self.head.next
        if headOld.key == key:
            return headOld.val
        node = self.map[key]
        pre = node.prev
        nex = node.next
        pre.next = nex
        nex.prev = pre
        self.head.next = node
        node.prev = self.head
        node.next = headOld
        headOld.prev = node
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.get(key)
            self.head.next.val = value
        else:
            headOld = self.head.next
            node = Node(key, value)
            self.head.next = node
            node.prev = self.head
            node.next = headOld
            headOld.prev = node
            self.map[key] = node
            self.count += 1
            if self.count > self.capacity:
                lastOld = self.last.prev
                lastNew = lastOld.prev
                lastNew.next = self.last
                self.last.prev = lastNew
                del self.map[lastOld.key]
                self.count -= 1
        return

obj = LRUCache(2)
obj.put(2,1)
obj.put(2,2)
print(obj.get(2))
obj.put(1,1)
obj.put(4,1)
print(obj.get(2))
