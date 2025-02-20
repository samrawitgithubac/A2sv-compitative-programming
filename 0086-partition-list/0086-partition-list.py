# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        current=dummy.next
        new=ListNode()
        curr=new
        ans=[]
        less=[]
        if head==None:
            return 
        while current:
            ans.append(current.val)
            current=current.next
        for i in range(len(ans)):
            if ans[i]<x:
                less.append(ans[i])
        for i in range(len(ans)):
            if ans[i] >=x:
                less.append(ans[i])
        print(less)
        for i in range(len(less)):
            if i == len(less)-1:
                curr.val = less[i]
                curr.next= None
            else:
                curr.val = less[i]
                curr.next = ListNode()
                curr=curr.next
        return new

                


        
        
        


