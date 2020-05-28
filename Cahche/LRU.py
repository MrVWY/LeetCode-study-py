class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = Node(key, value)

            self.cache[key] = node

            self.addHeadNode(node)
            self.size += 1
            if self.size > self.capacity:
                tails = self.removeTail()
                self.cache.pop(tails.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def addHeadNode(self, node):
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node

    def removerNode(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def moveToHead(self, node):
        self.removerNode(node)
        self.addHeadNode(node)

    def removeTail(self):
        node = self.tail.pre
        self.removerNode(node)
        return node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

from collections import OrderedDict


class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        self[key] = value
        self.move_to_end(key)
        if len(self) > self.capacity:
            self.popitem(last=False)
