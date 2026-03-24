class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.num_keys = 0
        self.head = None
        self.tail = None
        self.map = {}

    def get(self, key: int) -> int:
        if key in self.map:
            temp = self.map[key].val 
            self.remove(key)
            self.insert(key, temp)
            return temp
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(key)
        
        self.insert(key, value)
        if self.num_keys > self.capacity:
            self.remove(self.tail.key)
            
            
    def remove(self, key):
        node = self.map[key]
        if node == self.head:
            self.head = node.next
            if self.head:
                self.head.prev = None
        if node == self.tail:
            self.tail = node.prev
            if self.tail:
                self.tail.next = None
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        self.num_keys -= 1
        del self.map[key]

        return node
    
    def insert(self, key, val):
        self.map[key] = Node(key, val)
        node = self.map[key]
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            
        self.num_keys += 1
        return node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)