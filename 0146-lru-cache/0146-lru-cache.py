class Node:
    def __init__(self, key=-1, value=-1, next = None, prev= None):
        self.key = key
        self.val = value
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.pointers = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.pointers:
            node = self.pointers[key]
            self.remove(node)
            self.insertAtTail(node)
            return node.val
        return -1
        
    def remove(self, node):
        pr = node.prev
        nxt = node.next
        pr.next = nxt
        nxt.prev = pr
        key = node.key
        self.pointers.pop(key)

    def insertAtTail(self, node):
        key = node.key
        real_tail = self.tail.prev
        real_tail.next = node
        node.prev = real_tail
        node.next = self.tail
        self.tail.prev = node
        self.pointers[key] = node
        
    def put(self, key: int, value: int) -> None:
        if key in self.pointers:
            new_node = self.pointers[key]
            new_node.val = value
            self.remove(new_node)

        else:
            new_node = Node(key, value)
            num_nodes = len(self.pointers)

            if num_nodes == self.capacity:
                lru = self.head.next
                self.remove(lru)

        self.insertAtTail(new_node)

                






        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
