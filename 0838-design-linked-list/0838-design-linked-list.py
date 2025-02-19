class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.dummy = Node()
        self.tail = None
        self.size = 0 

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        else:
            cur_idx = 0
            current = self.dummy.next
            while cur_idx < index:
                current = current.next
                cur_idx += 1
            
            return current.value


    def addAtHead(self, val: int) -> None:
        head = self.dummy.next
        new_node = Node(val)
        self.dummy.next = new_node
        new_node.next = head
        self.size += 1
        
        # update tail
        if not self.tail:
            self.tail = new_node
        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.tail:
            self.dummy.next = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index == self.size:
            self.addAtTail(val)
        else:
            cur_idx = 0
            current = self.dummy
            while cur_idx < index:
                current = current.next
                cur_idx += 1
            new_node = Node(val)
            new_node.next = current.next
            current.next = new_node

            self.size += 1
            

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        cur_idx = 0
        current = self.dummy
        while cur_idx < index:
            current = current.next
            cur_idx += 1
        current.next = current.next.next

        # update tail
        if not current.next:
            self.tail = current

        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
