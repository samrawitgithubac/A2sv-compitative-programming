# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        current=head
        count=0
        sum=0
        while(current!=None):
            current=current.next
            count+=1
        current=head
        k=count-1
        while k>=0 and current!=None:
            sum+=current.val*pow(2,k)
            current=current.next
            k-=1
        return sum
        



        