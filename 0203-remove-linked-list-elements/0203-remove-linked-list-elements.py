# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Handle the case when the head node itself needs to be removed
        while head is not None and head.val == val:
            head = head.next
        
        current = head
        
        # Traverse the rest of the list
        while current is not None and current.next is not None:
            if current.next.val == val:
                # Skip the node with the value `val`
                current.next = current.next.next
            else:
                current = current.next
        
        return head
