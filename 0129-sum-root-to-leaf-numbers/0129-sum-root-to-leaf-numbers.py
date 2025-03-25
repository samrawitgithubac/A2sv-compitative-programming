# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans=[]
        
        def helper(n,num):
            if n==None:
                return 
            num.append(str(n.val))
            if n.left==None and n.right==None:
                ans.append(''.join(num))
                num.pop()
                return 
            helper(n.left,num)
            
            helper(n.right,num)
            num.pop()
        helper(root,[])
        ans=list(map(int,ans))
        return sum(ans)
        
      
            
            


        
            

        
       