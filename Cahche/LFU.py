import collections


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minFreq = 0
        self.size = 0
        self.cache = {}
        self.freqM = collections.defaultdict(create_link_list)

    def delete(self, node):
        if node.pre:
            node.pre.nex = node.nex
            node.nex.pre = node.pre
            if node.pre is self.freqM[node.freq][0] and node.nex is self.freqM[node.freq][-1]:  # 判断当前cache中是否只有这一个key
                self.freqM.pop(node.freq)
        return node.val

    def increase(self, node):
        node.freq += 1
        self.delete(node)
        self.freqM[node.freq][-1].pre.insert(node)
        if node.freq == 1:
            self.minFreq = 1
        elif self.minFreq == node.freq - 1:
            head, tail = self.freqM[node.freq - 1]
            if head.nex == tail:
                self.minFreq = node.freq

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.increase(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if self.capacity != 0:
            if key in self.cache:
                node = self.cache[key]
                node.val = value
            else:
                node = Node(key, value)
                self.cache[key] = node
                self.size += 1

            if self.size > self.capacity:
                self.size -= 1
                delete = self.delete(self.freqM[self.minFreq][0].nex)
                self.cache.pop(delete)
            self.increase(node)


class Node:
    def __init__(self, key, val, pre=None, nex=None, freq=0):
        self.key = key
        self.val = val
        self.pre = pre
        self.nex = nex
        self.freq = freq

    def insert(self, nex):
        nex.pre = self
        nex.nex = self.nex
        self.nex.pre = nex
        self.nex = nex


def create_link_list():
    head = Node(0, 0)
    tail = Node(0, 0)
    head.nex = tail
    tail.pre = head
    return head, tail

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
