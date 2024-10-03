# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = l1
        current2 = l2
        numSum = 0

        digit = 1
        while current1 != None:
            numSum += current1.val * digit
            digit *= 10

            current1 = current1.next

        digit = 1
        while current2 != None:
            numSum += current2.val * digit
            digit *= 10

            current2 = current2.next

        if numSum == 0:
            return ListNode(0)
        
        head = ListNode()
        current = head

        while numSum != 0:
            current.next = ListNode(numSum % 10)
            numSum = numSum // 10

            current = current.next

        return head.next        