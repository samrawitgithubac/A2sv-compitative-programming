# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr=head
        res=[]
        maxsums=float('-inf')
       
        while curr:
            res.append(curr.val)
            curr=curr.next
        l=0
        r=len(res)-1
        while l<r:
            maxsums=max(maxsums,res[l]+res[r])
            l+=1
            r-=1
        return  maxsums



        


       


        