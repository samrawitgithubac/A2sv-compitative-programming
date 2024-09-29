class MyLinkedList:
    
    class Node:  # Define a nested Node class
        def __init__(self, value: int):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None
        self.size = 0
                                                
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:  # Check for out-of-bounds
            return -1

        current = self.head
        while index > 0 and current:  # Use 'index' instead of 'n'
            current = current.next
            index -= 1

        return current.value if current else -1  # Return value or -1 if current is None

    def addAtHead(self, val: int) -> None:
        new_node = self.Node(val)  # Create a new node
        new_node.next = self.head
        self.head = new_node
        self.size += 1  # Update the size

    def addAtTail(self, val: int) -> None:
        new_node = self.Node(val)  # Create a new node with the given value
        
        if not self.head:  # If the list is empty, set the new node as the head
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = new_node  # Set the next pointer of the last node to the new node
            
        self.size += 1  # Update the size

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:  # Out of bounds
            return

        new_node = self.Node(val)  # Create a new node with the given value

        if index == 0:  # If adding at the head
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):  # Traverse to the node just before the index
                current = current.next
            new_node.next = current.next  # Insert the new node
            current.next = new_node

        self.size += 1  # Update the size

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:  # Out of bounds check
            return

        if index == 0:  # Handle head deletion
            self.head = self.head.next  # Update the head to the next node
        else:
            current = self.head
            for _ in range(index - 1):  # Traverse to the node just before the one to delete
                current = current.next
                if not current:  # Safety check in case the index is out of bounds
                    return
            if current.next:  # Ensure the next node exists before deleting
                current.next = current.next.next  # Bypass the node to delete

        self.size -= 1  # Decrease the size of the linked list


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index, val)
# obj.deleteAtIndex(index)
