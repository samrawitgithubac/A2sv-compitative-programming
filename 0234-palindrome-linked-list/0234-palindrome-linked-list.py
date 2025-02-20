# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        copyss = []
        temp = head
        while temp:
            copyss.append(temp.val)
            temp = temp.next

       
        dummy = ListNode(0, head)
        current = dummy.next
        pre = None
        while current:
            temp = current.next
            current.next = pre
            pre = current
            current = temp

        
        reversed_vals = []
        temp = pre
        while temp:
            reversed_vals.append(temp.val)
            temp = temp.next

        return copyss == reversed_vals  
